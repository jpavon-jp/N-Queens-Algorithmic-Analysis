# sa_nqueens.py 
import random
import time
import math
import psutil
import os

def count_conflicts(state):
    conflicts = 0
    N = len(state)
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def simulated_annealing(N, max_steps=50000, initial_temp=1000, cooling_rate=0.995):
    state = [random.randint(0, N - 1) for _ in range(N)]
    temperature = initial_temp
    steps = 0

    while temperature > 0.1 and steps < max_steps:
        current_conflicts = count_conflicts(state)
        if current_conflicts == 0:
            return state, steps, True

        row = random.randint(0, N - 1)
        col = random.randint(0, N - 1)
        while col == state[row]:
            col = random.randint(0, N - 1)

        new_state = state[:]
        new_state[row] = col
        new_conflicts = count_conflicts(new_state)
        delta = new_conflicts - current_conflicts

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            state = new_state[:]

        temperature *= cooling_rate
        steps += 1

    return state, steps, False

def solve_sa(N, attempts=10):
    best_result = None
    best_steps = float('inf')
    best_time = 0
    best_memory = 0
    found_solution = False

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt} for N={N}")
        start_time = time.time()
        process = psutil.Process(os.getpid())

        solution, steps, success = simulated_annealing(N)

        end_time = time.time()
        elapsed_time = end_time - start_time
        memory = process.memory_info().rss / (1024 * 1024)

        print(f"  Success: {success}")
        print(f"  Steps: {steps}")
        print(f"  Time: {elapsed_time:.4f} seconds")
        print(f"  Memory: {memory:.2f} MB")

        if success:
            found_solution = True
            best_result = solution
            best_steps = steps
            best_time = elapsed_time
            best_memory = memory
            break
        else:
            if steps < best_steps:
                best_result = solution
                best_steps = steps
                best_time = elapsed_time
                best_memory = memory

    print(f"\nFinal Result for N={N}")
    print(f"Success: {found_solution}")
    print(f"Steps: {best_steps}")
    print(f"Time: {best_time:.4f} seconds")
    print(f"Memory: {best_memory:.2f} MB")
    print(f"Solution: {best_result if found_solution else 'No solution'}\n")

    return best_result, found_solution, best_time, best_memory, best_steps

# Ejecutar para cada N
if __name__ == "__main__":
    for N in [10, 30, 50, 100, 200]:
        solve_sa(N)
