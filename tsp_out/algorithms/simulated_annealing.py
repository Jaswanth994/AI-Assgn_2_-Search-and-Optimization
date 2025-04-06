import random
import math
from utils.tsp_utils import total_distance, swap_two_cities, nearest_neighbor_heuristic

def simulated_annealing(cities, T=1000.0, alpha=0.995, T_min=1e-3):
    current = nearest_neighbor_heuristic(cities)
    best = current[:]
    current_distance = best_distance = total_distance(current)
    states = [current[:]]

    while T > T_min:
        neighbor = swap_two_cities(current)
        neighbor_distance = total_distance(neighbor)
        delta = neighbor_distance - current_distance

        if delta < 0 or math.exp(-delta / T) > random.random():
            current = neighbor
            current_distance = neighbor_distance
            states.append(current[:])
            if current_distance < best_distance:
                best = current
                best_distance = current_distance

        T *= alpha
    return best, best_distance, states
