import matplotlib.pyplot as plt
import os

def plot_performance(times, label, filename):
    os.makedirs("plots", exist_ok=True)
    plt.plot(times, marker='o', label=label)
    plt.xlabel("Run #")
    plt.ylabel("Time (s)")
    plt.title(f"{label} Performance")
    plt.legend()
    plt.savefig(f"plots/{filename}.png")
    plt.clf()
