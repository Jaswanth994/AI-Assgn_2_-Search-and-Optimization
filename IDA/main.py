import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from gymnasium.envs.toy_text.frozen_lake import FrozenLakeEnv, generate_random_map
from heuristic import manhattan_heuristic
from ida_star import ida_star
from plot_utils import plot_results
from video_utils import record_video

RUNS = 5
TIMEOUT_SECONDS = 60  # You can set this to 600 (10 min) if needed

times = []
steps = []

for i in range(RUNS):
    random_map = generate_random_map(size=4)
    env = FrozenLakeEnv(desc=random_map, is_slippery=False)

    start_time = time.time()
    solution, cost, visited = None, None, None

    with ThreadPoolExecutor() as executor:
        future = executor.submit(ida_star, env, manhattan_heuristic)
        try:
            solution, cost, visited = future.result(timeout=TIMEOUT_SECONDS)
            elapsed = time.time() - start_time
            times.append(elapsed)
            steps.append(len(solution) if solution else 0)
            print(f"✅ Run {i+1} | Time: {elapsed:.4f}s | Steps: {len(solution)}")
        except TimeoutError:
            elapsed = time.time() - start_time
            times.append(elapsed)
            steps.append(0)
            print(f"⏰ Run {i+1} TIMED OUT after {elapsed:.1f}s — No solution")

plot_results(times, steps)

# Only one video to avoid overwriting
record_video("gifs", ida_star, manhattan_heuristic)
