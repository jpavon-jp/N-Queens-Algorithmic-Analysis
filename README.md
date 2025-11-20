# ♛ N-Queens Algorithmic Analysis (DFS, HC, SA, GA)

A comparative study implementing four classical Artificial Intelligence search algorithms to solve the **N-Queens Problem**. The project benchmarks each algorithm's performance in terms of execution time, memory usage, and scalability across board sizes from **N=10** to **N=200**.

📄 **[Read the Full Research Report](./SS25___Machine_Learning_A___N_Queens___Josue_David_Pavon_Maldonado-2.pdf)**

---

## 📖 Project Overview
The N-Queens problem is a classic constraint satisfaction challenge. Instead of just solving it, this project treats it as a benchmark to evaluate different AI search paradigms:
1.  **Exhaustive Search:** Depth-First Search (DFS).
2.  **Greedy Search:** Hill Climbing (HC).
3.  **Probabilistic Search:** Simulated Annealing (SA).
4.  **Evolutionary Computation:** Genetic Algorithms (GA).

[cite_start]The study measures how each approach handles combinatorial explosion and local optima constraints [cite: 874-881].

---

## 📊 Key Findings & Benchmarks

| Algorithm | Type | Scalability | Success Rate (N=10-200) | Key Insight |
| :--- | :--- | :--- | :--- | :--- |
| **DFS** | Exact | Low | 50% (Failed > N=10) | Precise for small N, but computationally infeasible for large inputs due to exponential growth. |
| **Hill Climbing** | Greedy | Low | 0% (in tests) | Extremely fast but consistently trapped in local optima, failing to solve larger boards. |
| **Simulated Annealing** | Probabilistic | High | **60%** | The most robust performer. Effectively escaped local optima by allowing "bad moves" based on temperature. |
| **Genetic Algorithm** | Evolutionary | Medium | 20% | Scalable logic but required extensive tuning of population/mutation rates to converge. |

---

## 🛠️ Technical Stack

* **Language:** Python 3.11
* **Performance Monitoring:** `psutil` (Memory tracking), `time` (Execution speed).
* **Libraries:** `random`, `math`, `os`.
* **Concepts:** Constraint Satisfaction Problems (CSP), Heuristics, Optimization, Metaheuristics.

---

## 🚀 How to Run

Each algorithm is implemented in a standalone script.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jpavon-jp/N-Queens-Algorithmic-Analysis.git](https://github.com/jpavon-jp/N-Queens-Algorithmic-Analysis.git)
    ```
2.  **Run a specific solver (e.g., Simulated Annealing):**
    ```bash
    python sa_nqueens_JosuePavon.py
    ```
    *Note: The scripts are configured to auto-test N values [10, 30, 50, 100, 200].*

---

## ⚠️ Context
Developed for the **Machine Learning A** course (SS25) at the University of Europe for Applied Sciences.
**Author:** Josue David Pavon Maldonado
