

# 🧠 AI Assignment 2: Search and Optimization

This project implements and analyzes multiple **search and optimization algorithms** in different environments. The goal is to study their **performance**, **efficiency**, and **convergence behavior**.

---

## 📌 Assignment Objectives

- Implement and test the following algorithms:
  - **Branch and Bound (BnB)**
  - **Iterative Deepening A\***
  - **Hill Climbing (HC)**
  - **Simulated Annealing (SA)**

- Run experiments in:
  - **Frozen Lake Environment** (for BnB & IDA\*)
  - **Travelling Salesman Problem (TSP)** (for HC & SA)

- Record:
  - Average time taken
  - Convergence steps
  - Performance metrics across multiple runs

---

## 🗂️ Project Structure


ai-2/
├── BnB/
│   ├── main.py              # Entry point for BnB algorithm
│   ├── bnb.py
│   ├── heuristic.py
│   ├── plot_utils.py
│   └── video_utils.py
│
├── IDA/
│   ├── main.py              # Entry point for IDA* algorithm
│   ├── ida_star.py
│   ├── heuristic.py
│   ├── plot_utils.py
│   └── video_utils.py
│
└── tsp_out/
    ├── main.py              # Entry point for TSP (HC & SA)
    ├── algorithms/
    │   ├── hill_climbing.py
    │   └── simulated_annealing.py
    └── utils/
        ├── tsp_utils.py
        ├── plot_utils.py
        └── gif_utils.py


## Setup Instructions

### Requirements

Make sure you have **Python 3.8+** installed. Then install the required dependencies:

```bash
pip install gymnasium matplotlib numpy imageio[ffmpeg]
```

## How to Run the Algorithms

### 1. Branch and Bound (Frozen Lake)

```bash
cd BnB
python main.py
```

- Environment: Frozen Lake (custom generated maps)
- Heuristic: Manhattan distance
- Output: Graphs + optional video of agent's path
- Timeout: 10 minutes per run

### 2. Iterative Deepening A* (Frozen Lake)

```bash
cd IDA
python main.py
```

- Environment: Frozen Lake
- Heuristic: Manhattan distance
- Output: Graphs + optional video
- Runs averaged over 5 executions

### 3. Hill Climbing & Simulated Annealing (TSP)

```bash
cd tsp_out
python main.py
```

- Problem: Randomly generated TSP instances (cities)
- Output: Performance graphs and solution paths
- Separate runs for HC and SA included in one main file

## Results & Observations

### Branch and Bound (BnB)
- **Environment:** Frozen Lake  
- **Performance:** Slower convergence, prone to timeouts on larger maps  
- **Reason:** Explores multiple branches without good heuristics; becomes inefficient in complex maps  
- **Observation:** Not optimal for stochastic or trap-laden environments like Frozen Lake

### Iterative Deepening A* (IDA*)
- **Environment:** Frozen Lake  
- **Performance:** Fast, consistent convergence (often within 6 steps)  
- **Reason:** Combines DFS space-efficiency with heuristic guidance  
- **Observation:** Very reliable; optimal for grid-based deterministic navigation

### Hill Climbing (HC)
- **Environment:** TSP  
- **Performance:** Quick but inconsistent; often stuck in local optima  
- **Reason:** Greedy approach lacks exploration; poor global search  
- **Observation:** Not reliable for complex or large TSPs

### Simulated Annealing (SA)
- **Environment:** TSP  
- **Performance:** Slower start but better final results  
- **Reason:** Probabilistic jumps allow escape from local optima  
- **Observation:** Superior to HC in TSP; balances exploration & exploitation

## Extras

- **GIF/Video Recording**:
  - Frozen Lake runs include optional `.mp4` recordings using `video_utils.py`.
  - TSP solutions can be saved as `.gif` animations using `gif_utils.py`.

## Notes

- Each `main.py` includes multiple test runs (5x) for performance averaging.
- Timeout (τ) for each run is adjustable in `main.py` (default: 10 minutes).
- Heuristics used:
  - Frozen Lake: Manhattan distance
  - TSP: Euclidean distance

## Authors

- **G Nishchith** (Roll No: CS22B021)
- **G Jaswanth** (Roll No: CS22B020)

```