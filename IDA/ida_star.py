from collections import deque

def ida_star(env, heuristic_fn):
    start = env.reset()[0]
    goal = 15  # Assuming 4x4 map

    def dfs(path, g, bound, visited):
        current = path[-1]
        f = g + heuristic_fn(current)
        if f > bound:
            return f, None
        if current == goal:
            return f, path

        min_bound = float('inf')
        for a in range(env.action_space.n):
            env.unwrapped.s = current
            next_state, _, done, _, _ = env.step(a)

            if next_state in visited:
                continue

            visited.add(next_state)
            path.append(next_state)
            t, result = dfs(path, g + 1, bound, visited)
            if result is not None:
                return t, result
            path.pop()
            visited.remove(next_state)

        return min_bound, None

    bound = heuristic_fn(start)
    path = [start]
    visited = set([start])
    while True:
        t, result = dfs(path, 0, bound, visited)
        if result is not None:
            # Reconstruct actions
            actions = []
            for i in range(len(result)-1):
                env.unwrapped.s = result[i]
                for a in range(env.action_space.n):
                    env.unwrapped.s = result[i]
                    s2, _, _, _, _ = env.step(a)
                    if s2 == result[i+1]:
                        actions.append(a)
                        break
            return actions, len(result)-1, len(result)
        if t == float('inf'):
            return None, float('inf'), len(visited)
        bound = t
