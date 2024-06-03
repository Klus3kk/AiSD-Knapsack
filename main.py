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
        n = int(input('Liczba przedmiotów: '))
        C = int(input('Pojemność plecaka: '))
        filename = input('Nazwa pliku wyjściowego: ')
        generate_knapsack_data(filename, n, C)
        print(f"Dane wygenerowane i zapisane do {filename}")
    elif cmd == 'load':
        filename = input('Nazwa pliku do załadowania danych: ')
        global data
        data['C'], data['n'], data['weights'], data['values'], data['items'] = load_knapsack_data(filename)
        print(f"Dane załadowane z {filename}")
    elif cmd == 'run':
        if 'C' in data and 'n' in data and 'values' in data and 'weights' in data and 'items' in data:
            time_dynamic, time_brute_force = measure_performance(data['C'], data['weights'], data['values'], data['n'], data['items'])
            print(f"Czas dla programowania dynamicznego: {time_dynamic}")
            print(f"Czas dla brute force: {time_brute_force}")
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
