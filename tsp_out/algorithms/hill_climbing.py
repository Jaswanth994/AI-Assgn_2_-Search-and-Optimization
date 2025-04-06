from utils.tsp_utils import total_distance, swap_two_cities, nearest_neighbor_heuristic

def hill_climbing(cities):
    # Start with a heuristic-based path
    current = nearest_neighbor_heuristic(cities)
    current_distance = total_distance(current)

    improved = True
    states = [current[:]]  # Store states for GIF generation

    while improved:
        improved = False
        for _ in range(100):
            neighbor = swap_two_cities(current)
            neighbor_distance = total_distance(neighbor)

            if neighbor_distance < current_distance:
                current = neighbor
                current_distance = neighbor_distance
                states.append(current[:])
                improved = True
                break  # Accept the first improvement

    return current, current_distance, states
