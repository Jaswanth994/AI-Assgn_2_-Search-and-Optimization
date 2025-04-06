import random
import math

def generate_cities(n=25, seed=None):
    if seed is not None:
        random.seed(seed)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

def total_distance(cities):
    return sum(
        math.dist(cities[i], cities[(i + 1) % len(cities)])
        for i in range(len(cities))
    )

def swap_two_cities(route):
    a, b = random.sample(range(len(route)), 2)
    new_route = route[:]
    new_route[a], new_route[b] = new_route[b], new_route[a]
    return new_route

def nearest_neighbor_heuristic(cities):
    unvisited = cities[:]
    route = [unvisited.pop(0)]
    while unvisited:
        next_city = min(unvisited, key=lambda city: math.dist(route[-1], city))
        route.append(next_city)
        unvisited.remove(next_city)
    return route
