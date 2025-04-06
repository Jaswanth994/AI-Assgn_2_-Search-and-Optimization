import matplotlib.pyplot as plt
import os

def plot_results(times, steps):
    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(times, marker='o')
    plt.title("Time per Run")
    plt.xlabel("Run #")
    plt.ylabel("Time (s)")

    plt.subplot(1, 2, 2)
    plt.plot(steps, marker='x', color='green')
    plt.title("Steps to Goal")
    plt.xlabel("Run #")
    plt.ylabel("Steps")

    plt.tight_layout()
    plt.savefig("plots/performance.png")
    plt.show()
