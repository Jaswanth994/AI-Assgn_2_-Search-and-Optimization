def manhattan_heuristic(state, goal=15):
    row1, col1 = divmod(state, 4)
    row2, col2 = divmod(goal, 4)
    return abs(row1 - row2) + abs(col1 - col2)
