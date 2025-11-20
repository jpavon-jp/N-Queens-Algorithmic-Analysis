# greedy_nqueens.py 
import random
import time
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

def hill_climbing(N, max_steps=1000):
    state = [random.randint(0, N - 1) for _ in range(N)]
    steps = 0

    while steps < max_steps:
        conflicts = count_conflicts(state)
        if conflicts == 0:
            return state, steps, True

        min_conflicts = conflicts
        best_state = state[:]

        for row in range(N):
            original_col = state[row]
            for col in range(N):
                if col == original_col:
                    continue
                state[row] = col
                new_conflicts = count_conflicts(state)
                if new_conflicts < min_conflicts:
                    min_conflicts = new_conflicts
                    best_state = state[:]
            state[row] = original_col

        if best_state == state:
            break  # stuck in local minimum
        else:
            state = best_state[:]

        steps += 1

    return state, steps, False

def solve_hill_climbing(N, attempts=5):
    best_result = None
    best_steps = float('inf')
    best_time = 0
    best_memory = 0
    found_solution = False

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt} for N={N}")
        start_time = time.time()
        process = psutil.Process(os.getpid())

        solution, steps, success = hill_climbing(N)

        end_time = time.time()
        elapsed_time = end_time - start_time
        memory = process.memory_info().rss / (1024 * 1024)

        print(f"  Success: {success}")
        print(f"  Steps: {steps}")
        print(f"  Time: {elapsed_time:.4f} seconds")
        print(f"  Memory: {memory:.2f} MB\n")

        if success:
            found_solution = True
            best_result = solution
            best_steps = steps
            best_time = elapsed_time
            best_memory = memory
            break  # Exit early if solution is found
        else:
            if steps < best_steps:
                best_result = solution
                best_steps = steps
                best_time = elapsed_time
                best_memory = memory

    print(f"Final Result for N={N}")
    print(f"Success: {found_solution}")
    print(f"Steps: {best_steps}")
    print(f"Time: {best_time:.4f} seconds")
    print(f"Memory: {best_memory:.2f} MB")
    print(f"Solution: {best_result if found_solution else 'No solution'}\n")

    return best_result, found_solution, best_time, best_memory, best_steps

# Execute for all desired N
if __name__ == "__main__":
    for N in [10, 30, 50, 100, 200]:
        solve_hill_climbing(N)
