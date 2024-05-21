import random

def generate_knapsack_data(filename, n, C):
    items = [(random.randint(1, 20), random.randint(1, 100)) for _ in range(n)]
    with open(filename, 'w') as f:
        f.write(f"{C}\n")
        f.write(f"{n}\n")
        for p, w in items:
            f.write(f"{p} {w}\n")

def load_knapsack_data(filename):
    with open(filename, 'r') as f:
        C = int(f.readline().strip())
        n = int(f.readline().strip())
        items = [tuple(map(int, line.strip().split())) for line in f.readlines()]
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    return C, n, values, weights

def knapsack_dynamic(C, weights, values, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][C]

from itertools import combinations

def knapsack_brute_force(C, weights, values, n):
    max_value = 0
    for i in range(n + 1):
        for combo in combinations(range(n), i):
            weight_sum = sum(weights[j] for j in combo)
            value_sum = sum(values[j] for j in combo)
            if weight_sum <= C and value_sum > max_value:
                max_value = value_sum
    return max_value

def measure_performance(C, weights, values, n):
    import time

    start_time = time.time()
    result_dynamic = knapsack_dynamic(C, weights, values, n)
    time_dynamic = time.time() - start_time

    start_time = time.time()
    result_brute_force = knapsack_brute_force(C, weights, values, n)
    time_brute_force = time.time() - start_time

    return time_dynamic, time_brute_force
