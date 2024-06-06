import random

# Definiujemy elementy muzyczne z ich odpowiednimi wartościami i wagami
music_items = [
    ("Kaseta", 1, 10),   # (name, weight, value)
    ("Winyl", 5, 50),
    ("CD", 2, 20),
    ("Album Cyfrowy", 1, 15),
    ("Bilet na koncert", 1, 100),
    ("Kostka do gitary", 1, 5),
    ("Plakat", 1, 30),
    ("Słuchawki", 2, 70),
    ("Głośnik", 3, 80),
    ("Mikrofon", 2, 40),
    ("Mikserek", 3, 90),
    ("Stroik", 1, 10),
    ("Tamburyn", 1, 25),
    ("Klarnet", 2, 60),
    ("Gitara", 4, 120),
    ("Keyboard", 5, 150),
    ("Bębny", 6, 200),
    ("Saksofon", 3, 85),
    ("Perkusja", 10, 300),
    ("Zestaw płyt CD", 2, 35)
]

def generate_knapsack_data(filename, n, C):
    if n > len(music_items):
        raise ValueError("Liczba przedmiotów przekracza liczbę dostępnych przedmiotów.")
    
    selected_items = random.sample(music_items, n)
    with open(filename, 'w') as f:
        f.write(f"{C}\n")
        f.write(f"{n}\n")
        for item in selected_items:
            f.write(f"{item[1]} {item[2]}\n")

def load_knapsack_data(filename):
    with open(filename, 'r') as f:
        C = int(f.readline().strip())
        n = int(f.readline().strip())
        items = [tuple(map(int, line.strip().split())) for line in f.readlines()]
    weights = [item[0] for item in items]
    values = [item[1] for item in items]
    return C, n, weights, values, items

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
    return K[n][C], get_selected_items_dynamic(K, weights, n, C)

def get_selected_items_dynamic(K, weights, n, C):
    selected_items = []
    w = C
    for i in range(n, 0, -1):
        if K[i][w] != K[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    return selected_items

from itertools import combinations

def knapsack_brute_force(C, weights, values, n):
    max_value = 0
    best_combination = []
    for i in range(n + 1):
        for combo in combinations(range(n), i):
            weight_sum = sum(weights[j] for j in combo)
            value_sum = sum(values[j] for j in combo)
            if weight_sum <= C and value_sum > max_value:
                max_value = value_sum
                best_combination = combo
    return max_value, best_combination

def measure_performance(C, weights, values, n, item_names):
    import time

    start_time = time.time()
    selected_items_dynamic = knapsack_dynamic(C, weights, values, n)
    time_dynamic = time.time() - start_time

    start_time = time.time()
    selected_items_brute_force = knapsack_brute_force(C, weights, values, n)
    time_brute_force = time.time() - start_time

    print("\nWyniki Programowania Dynamicznego:")
    display_selected_items(item_names, selected_items_dynamic, weights, values)
    
    print("\nWyniki Brute Force:")
    display_selected_items(item_names, selected_items_brute_force, weights, values)

    return time_dynamic, time_brute_force

def display_selected_items(item_names, selected_indices, weights, values):
    print("Wybrane przedmioty:")
    total_weight = 0
    total_value = 0
    for index in selected_indices:
        item = item_names[index]
        weight = weights[index]
        value = values[index]
        total_weight += weight
        total_value += value
        print(f"{item[0]} (waga: {weight}, wartość: {value})")
    print(f"Całkowita waga: {total_weight}")
    print(f"Całkowita wartość: {total_value}")
