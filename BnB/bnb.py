from queue import PriorityQueue

def branch_and_bound(env, heuristic_fn):
    start = env.reset()[0]
    best_cost = {start: 0}
    frontier = PriorityQueue()
    frontier.put((heuristic_fn(start), 0, start, []))  # (bound, cost, state, path)

    nodes_visited = 0
    best_solution = None
    best_solution_cost = float("inf")

    while not frontier.empty():
        bound, cost, current, path = frontier.get()

        # Prune if bound exceeds best solution cost
        if bound >= best_solution_cost:
            continue

        nodes_visited += 1

        if current == 15:
            best_solution = path
            best_solution_cost = cost
            continue

        for a in range(env.action_space.n):
            env.unwrapped.s = current
            next_state, _, done, _, _ = env.step(a)
            new_cost = cost + 1

            if new_cost < best_cost.get(next_state, float('inf')):
                best_cost[next_state] = new_cost
                new_bound = new_cost + heuristic_fn(next_state)
                frontier.put((new_bound, new_cost, next_state, path + [a]))

    return best_solution, best_solution_cost, nodes_visited



