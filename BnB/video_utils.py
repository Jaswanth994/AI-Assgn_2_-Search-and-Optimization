import gymnasium as gym
from gymnasium.wrappers import RecordVideo
import os

# def record_video(path, bnb_func, heuristic_fn, custom_map=None):
#     os.makedirs(path, exist_ok=True)
#     env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array",
#                    desc=custom_map if custom_map else None,
#                    map_name="4x4")

#     env = RecordVideo(env, video_folder=path, episode_trigger=lambda x: True)

#     state = env.reset()[0]
#     solution, _, _ = bnb_func(env, heuristic_fn)

#     if solution is None:
#         print("❌ No solution found.")
#         env.close()
#         return

#     for a in solution:
#         env.step(a)

#     env.close()
#     print("🎥 Video recorded at:", path)


def record_video(path, bnb_func, heuristic_fn, desc=None):
    os.makedirs(path, exist_ok=True)
    if desc is None:
        from gymnasium.envs.toy_text.frozen_lake import generate_random_map
        desc = generate_random_map(size=4)

    env = gym.make("FrozenLake-v1", desc=desc, is_slippery=False, render_mode="rgb_array")
    env = RecordVideo(env, video_folder=path, episode_trigger=lambda x: True)

    print("\n🎥 Recording video on map:")
    for row in desc:
        print("".join(row))

    state = env.reset()[0]
    solution, _, _ = bnb_func(env, heuristic_fn)

    if solution is None:
        print("❌ No solution found.")
        env.close()
        return

    for a in solution:
        env.step(a)

    env.close()
    print("🎞️ Video recorded at:", path)
