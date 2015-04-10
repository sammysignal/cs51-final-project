# Application of a Genetic Algorithm to Rooming Optimization

## Introduction and Overview 
The essential problem that this project will address is that of optimizing a variety of preferences and requirements within certain constraints. In other words, finding an “ideal” solution among many, many possibilities. In this case, we will be applying a genetic algorithm to best sort incoming Harvard freshman into rooming accommodations that fit their preferences, not just with regard to the rooms themselves but also with regard to their roommates. 

Before matriculating at Harvard, all incoming freshman are required to take a housing survey. Data points from this survey will be used to best match students with rooms and roommates. Our goal is to apply a genetic algorithm to this process to achieve an “optimized” assignment scheme that best satisfies student preferences. Provided the aforementioned data points, the algorithm will first create a population of a number of random solution candidates. The fitness of each of the candidates will be assessed, after which a new population will be created by breeding the fittest candidates. Once a certain fitness level is reached, or a certain number of population “breedings” in reached, a final rooming configuration will be submitted.
