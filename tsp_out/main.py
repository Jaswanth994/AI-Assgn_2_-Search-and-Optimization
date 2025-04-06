import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from utils.tsp_utils import generate_cities
from utils.plot_utils import plot_performance
from utils.gif_utils import save_gif

TIMEOUT = 10 * 60  # 10 minutes
RUNS = 5
N_CITIES = 20

def run_with_timeout(func, cities):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(func, cities)
        try:
            start = time.time()
            result, dist, states = future.result(timeout=TIMEOUT)
            end = time.time()
            return end - start, dist, states
        except TimeoutError:
            return TIMEOUT, None, []

def main():
    hc_times, sa_times = [], []

    for i in range(RUNS):
        cities = generate_cities(N_CITIES, seed=i)
        t1, _, hc_states = run_with_timeout(hill_climbing, cities)
        t2, _, sa_states = run_with_timeout(simulated_annealing, cities)

        hc_times.append(t1)
        sa_times.append(t2)

        print(f"Run {i+1}: HC Time = {t1:.2f}s, SA Time = {t2:.2f}s")
        save_gif(hc_states, f"hc_run{i+1}")
        save_gif(sa_states, f"sa_run{i+1}")

    plot_performance(hc_times, "Hill Climbing", "hc")
    plot_performance(sa_times, "Simulated Annealing", "sa")

if __name__ == "__main__":
    main()
