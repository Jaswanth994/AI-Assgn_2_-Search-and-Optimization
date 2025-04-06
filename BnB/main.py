import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from gymnasium.envs.toy_text.frozen_lake import FrozenLakeEnv
from heuristic import manhattan_heuristic
from bnb import branch_and_bound
from plot_utils import plot_results
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from video_utils import record_video

USE_CUSTOM_MAP = True
CUSTOM_MAP = [
    "SFFF",
    "FHFH",
    "FFFH",
    "HFFG"
]

RUNS = 5
TIMEOUT_SECONDS = 10 * 60  # 10 minutes

times = []
steps = []

# for i in range(RUNS):
#     env = FrozenLakeEnv(desc=CUSTOM_MAP if USE_CUSTOM_MAP else None, map_name="4x4", is_slippery=False)
#     start_time = time.time()

#     solution, cost, visited = None, None, None
#     with ThreadPoolExecutor() as executor:
#         future = executor.submit(branch_and_bound, env, manhattan_heuristic)
#         try:
#             solution, cost, visited = future.result(timeout=TIMEOUT_SECONDS)
#             elapsed = time.time() - start_time
#             times.append(elapsed)
#             steps.append(len(solution) if solution else 0)
#             print(f"✅ Run {i+1} | Time: {elapsed:.4f}s | Steps: {len(solution)}")
#         except TimeoutError:
#             elapsed = time.time() - start_time
#             times.append(elapsed)
#             steps.append(0)
#             print(f"⏰ Run {i+1} TIMED OUT after {elapsed:.1f}s — No solution")

# plot_results(times, steps)

# # Record only if solution exists
# if any(steps):
#     record_video("gifs", branch_and_bound, manhattan_heuristic,
#                  custom_map=CUSTOM_MAP if USE_CUSTOM_MAP else None)


for i in range(RUNS):
    random_map = generate_random_map(size=4)
    env = FrozenLakeEnv(desc=random_map, is_slippery=False)

    print(f"\n🧊 Run {i+1} — Random Map:")
    for row in random_map:
        print("".join(row))

    start_time = time.time()
    solution, cost, visited = None, None, None
    with ThreadPoolExecutor() as executor:
        future = executor.submit(branch_and_bound, env, manhattan_heuristic)
        try:
            solution, cost, visited = future.result(timeout=TIMEOUT_SECONDS)
            elapsed = time.time() - start_time
            times.append(elapsed)
            steps.append(len(solution) if solution else 0)
            print(f"✅ Run {i+1} | Time: {elapsed:.4f}s | Steps: {len(solution)} | Nodes visited: {visited}")
        except TimeoutError:
            elapsed = time.time() - start_time
            times.append(elapsed)
            steps.append(0)
            print(f"⏰ Run {i+1} TIMED OUT after {elapsed:.1f}s — No solution")

    # 🎥 Record each run's video
    video_path = f"gifs/run{i+1}"
    record_video(video_path, branch_and_bound, manhattan_heuristic, desc=random_map)


