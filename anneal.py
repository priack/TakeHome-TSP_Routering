import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from util import read_cities, visualize_tsp, path_cost


class SimAnneal:
    def __init__(self, cities, temperature=None, alpha=None, stopping_temperature=None, stopping_iter=None, initializer=None):
        self.cities = cities
        self.num_cities = len(cities)
        self.temperature = math.sqrt(self.num_cities) if not temperature else temperature
        self.alpha = 0.999 if not alpha else alpha
        self.stopping_temperature = 1e-8 if not stopping_temperature else stopping_temperature
        self.stopping_iter = 100000 if not stopping_iter else stopping_iter
        self.iteration = 1
        self.route = None
        self.best_fitness = float("Inf")
        self.progress = []
        self.cur_cost = None
        self.best_iteration = 0
        if initializer== 'random' or None:
            self.initializer = self.get_initial_solution
        else:
            self.initializer = self.greedy_solution
        self.distances = np.zeros((self.num_cities, self.num_cities)) + np.Inf
        for i, c1 in enumerate(cities):
            for j in range(i + 1, self.num_cities):
                self.distances[i, j] = c1.distance(cities[j])
                self.distances[j, i] = self.distances[i, j]

    def get_initial_solution(self):
        random_indices = random.sample(range(self.num_cities), self.num_cities)
        random_route = [self.cities[i] for i in random_indices]

        current_cost = path_cost(random_route)
        return random_route, current_cost


    def greedy_solution(self):
        visited = [np.random.randint(self.num_cities)]
        for i in range(63):
            last = visited[-1]
            node = np.argmin(self.distances[last, :])
            self.distances[last, :] = np.Inf
            self.distances[:, last] = np.Inf
            visited += [node]
        route = [self.cities[i] for i in visited]
        current_cost = path_cost(route)
        return route, current_cost

    def accept_probability(self, candidate_fitness):
        return math.exp(-abs(candidate_fitness - self.cur_cost) / self.temperature)

    def accept(self, guess):
        guess_cost = path_cost(guess)
        if guess_cost < self.cur_cost:
            self.cur_cost, self.route = guess_cost, guess
            if guess_cost < self.best_fitness:
                self.best_fitness, self.route = guess_cost, guess
                self.best_iteration = self.iteration
        else:
            if random.random() < self.accept_probability(guess_cost):
                self.cur_cost, self.route = guess_cost, guess

    def update_temperature(self):
        self.temperature *= self.alpha

    def run(self):
        self.route, self.cur_cost = self.initializer()
        self.best_fitness = self.cur_cost
        while self.temperature >= self.stopping_temperature and self.iteration < self.stopping_iter:
            guess = list(self.route)
            start_index = random.randint(2, self.num_cities - 1)
            end_index = random.randint(start_index, self.num_cities)
            guess[start_index: end_index] = reversed(guess[start_index: end_index])
            self.accept(guess)
            self.iteration += 1
            self.progress.append(self.cur_cost)
            if self.iteration % 100 == 0:
                self.update_temperature()

        print("Best fitness obtained: ", self.best_fitness)

    def visualize_routes(self):
        visualize_tsp('simulated annealing TSP', self.route)

    def plot_learning(self):
        plt.figure(1)
        plt.plot([i for i in range(len(self.progress))], self.progress)
        plt.ylabel("Distance")
        plt.xlabel("Iterations")
        plt.show(block=False)


if __name__ == "__main__":
    cities = read_cities(64)
    nRep = 30
    # Method, repetition
    speed = np.zeros((2, nRep, 2))
    for r in range(nRep):
        sa = SimAnneal(cities, stopping_iter=50000)
        sa.run()
        speed[0, r, 0] = sa.cur_cost
        speed[0, r, 1] = sa.best_iteration
        sa = SimAnneal(cities, stopping_iter=50000, initializer='greedy')
        sa.run()
        speed[1, r, 0] = sa.cur_cost
        speed[1, r, 1] = sa.best_iteration
