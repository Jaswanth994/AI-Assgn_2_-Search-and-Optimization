import gymnasium as gym
from gymnasium.wrappers import RecordVideo
import os
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

def record_video(path, ida_func, heuristic_fn):
    os.makedirs(path, exist_ok=True)
    random_map = generate_random_map(size=4)
    env = gym.make("FrozenLake-v1", desc=random_map, is_slippery=False, render_mode="rgb_array")
    env = RecordVideo(env, video_folder=path, episode_trigger=lambda ep: True)

    state = env.reset()[0]
    solution, _, _ = ida_func(env, heuristic_fn)

    if solution is None:
        print("❌ No solution found.")
        env.close()
        return

    for a in solution:
        env.step(a)

    env.close()
    print("🎥 Video recorded at:", path)
