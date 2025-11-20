# ga_nqueens.py
import random
import time
import psutil
import os

def fitness(state):
    N = len(state)
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return -conflicts  # higher is better

def crossover(parent1, parent2):
    N = len(parent1)
    point = random.randint(0, N - 1)
    return parent1[:point] + parent2[point:]

def mutate(state, mutation_rate=0.1):
    N = len(state)
    for i in range(N):
        if random.random() < mutation_rate:
            state[i] = random.randint(0, N - 1)
    return state

def genetic_algorithm(N, population_size=100, generations=1000, mutation_rate=0.1):
    population = [[random.randint(0, N - 1) for _ in range(N)] for _ in range(population_size)]

    for generation in range(generations):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == 0:
            return population[0], generation, True

        new_population = population[:20]  # elitismo

        while len(new_population) < population_size:
            p1 = random.choice(population[:50])
            p2 = random.choice(population[:50])
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return population[0], generations, False

def solve_ga(N):
    start_time = time.time()
    process = psutil.Process(os.getpid())

    solution, generations, success = genetic_algorithm(N)

    end_time = time.time()
    elapsed_time = end_time - start_time
    memory = process.memory_info().rss / (1024 * 1024)

    print(f"Genetic Algorithm for N={N}")
    print(f"Success: {success}")
    print(f"Generations: {generations}")
    print(f"Time: {elapsed_time:.4f} seconds")
    print(f"Memory: {memory:.2f} MB")
    print(f"Solution: {solution if success else 'No solution'}\n")

    return solution, success, elapsed_time, memory, generations

if __name__ == "__main__":
    for N in [10, 30, 50, 100, 200]:
        solve_ga(N)
