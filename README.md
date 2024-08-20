# TakeHome-TSP_Routering
## Problem
You are an AI engineer designing a routeing algorithm that will be used to determine
where new transmission lines should be built. This algorithm will solve a routeing
optimisation problem using real geospatial data.

Your task is to investigate and discuss different approaches to solving this problem.
From a high level, investigate different approaches to solving this problem and come
prepared to discuss your findings. You can choose whatever presentation format you’re most
comfortable with.

Some considerations that should factor into your research:
- Routes should take as few turns as possible
- Routes should avoid areas of constraints
- Routes should minimise crossings with existing infrastructure
- Ideally we would like to explore more than one routeing option
- How will the algorithm scale as the size of the problem scales? For example, if the
routes become longer.
- How easily will the proposed solution allow for changes to the costing assumptions?
For example, what if we then want to start placing limits on route curvature?
- In what format should the geospatial data be fed to the algorithm? What scaling and
performance implications does this have on the overall solution?

Your presentation should also cover how you would tackle this problem in practice, such as
whether you would set up any experiments to compare different approaches, the pros and
cons and flexibility of each approach, and which you would advocate for.

This will be high level, so there is no need to produce any code or even pseudocode.
## Available data
- You have a start point and an endpoint, defined on a map.
- You have a number of urban and rural geospatial data sources available. For this
exercise, assume that you will have access to commonly available data:
  - Locations of residential and commercial buildings
  - Parks
  - Farmland
  - Woodland
  - Terrain (elevation, slope etc)
  - Surface water
  - Locations of existing linear infrastructure, such as:
    - Different types of roads (motorways, A roads, B roads, etc)
    - Railway lines
    - Pipelines
    - Transmission lines
