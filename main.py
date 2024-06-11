import sys
from knapsack import generate_knapsack_data, load_knapsack_data, measure_performance, music_items

data = {}

def display_help():
    print("\nDostępne polecenia:")
    print("Help       - Wyświetl tę wiadomość")
    print("Generate   - Wygeneruj dane dla problemu plecakowego")
    print("Load       - Załaduj dane z pliku")
    print("Run        - Uruchom algorytmy i porównaj wyniki")
    print("Exit       - Wyjście z programu (takie samo jak Ctrl+C)")

def process_command(command):
    args = command.split()
    cmd = args[0].lower()

    if cmd == 'help':
        display_help()
    elif cmd == 'generate':
        if len(args) > 1:
            filename = args[1]
        else:
            filename = input('Nazwa pliku wyjściowego: ')

        # Sprawdzenie ograniczeń PRZED pytaniem o dane
        max_items = len(music_items)
        max_capacity = sum([item[1] for item in music_items])

        while True:  # Pętla, dopóki nie podamy poprawnych danych
            try:
                n = int(input(f'Liczba przedmiotów (max {max_items}): '))
                if not (1 <= n <= max_items):  # Sprawdzamy zakres
                    raise ValueError(f"Liczba przedmiotów musi być z zakresu 1-{max_items}")

                C = int(input(f'Pojemność plecaka (max {max_capacity}): '))
                if not (1 <= C <= max_capacity):  # Sprawdzamy zakres
                    raise ValueError(f"Pojemność plecaka musi być z zakresu 1-{max_capacity}")

                break  # Wychodzimy z pętli, jeśli dane są poprawne
            except ValueError as e:
                print(f"Błąd: {e}")

        generate_knapsack_data(filename, n, C)
        print(f"Dane wygenerowane i zapisane do {filename}")
    elif cmd == 'load':
        if len(args) > 1:
            filename = args[1]
        else:
            filename = input('Nazwa pliku do załadowania danych: ')

        # Upewniamy się, że plik ma rozszerzenie .txt
        if not filename.endswith('.txt'):
            filename += '.txt'

        global data
        try:
            data['C'], data['n'], data['weights'], data['values'], _ = load_knapsack_data(filename)
            data['items'] = music_items[:data['n']]
            print(f"Dane załadowane z {filename}")
        except FileNotFoundError:
            print(f"Plik {filename} nie został znaleziony.")
    elif cmd == 'run':
        if 'C' in data and 'n' in data and 'values' in data and 'weights' in data and 'items' in data:
            time_dynamic, time_brute_force = measure_performance(data['C'], data['weights'], data['values'], data['n'], data['items'])
            print(f"\nCzas dla programowania dynamicznego: {time_dynamic:.6f} sekund")
            print(f"Czas dla brute force: {time_brute_force:.6f} sekund")
        else:
            print("Dane nie zostały załadowane. Użyj polecenia 'Load' najpierw.")
    elif cmd == 'exit':
        print('Wychodzenie...')
        sys.exit(0)
    else:
        print('Nieprawidłowe polecenie. Wpisz "help" aby uzyskać listę poleceń.')

def main():
    while True:
        try:
            command = input('\naction> ')
            process_command(command)
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

if __name__ == '__main__':
    main()
