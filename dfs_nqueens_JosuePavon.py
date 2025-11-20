# dfs_nqueens.py
import time
import psutil
import os

solutions = []

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def dfs(board, row, N):
    if row == N:
        solutions.append(board[:])
        return True  # Stop after first solution

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if dfs(board, row + 1, N):
                return True
    return False

def solve_n_queens_dfs(N):
    board = [-1] * N
    start_time = time.time()
    process = psutil.Process(os.getpid())
    dfs(board, 0, N)
    end_time = time.time()

    elapsed_time = end_time - start_time
    memory_usage = process.memory_info().rss / (1024 * 1024)  # in MB
    result = solutions[0] if solutions else None

    print(f"DFS Result for N={N}:")
    print(f"Solution: {result}")
    print(f"Time: {elapsed_time:.4f} seconds")
    print(f"Memory: {memory_usage:.2f} MB")
    return result, elapsed_time, memory_usage

# Example run
if __name__ == "__main__":
    for N in [10, 30]:
        solutions.clear()
        print("\n===========================")
        solve_n_queens_dfs(N)

