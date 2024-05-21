import sys
from knapsack import generate_knapsack_data, load_knapsack_data, measure_performance

data = {}

def display_help():
    print("\nAvailable commands:")
    print("Help       - Show this message")
    print("Generate   - Generate knapsack data")
    print("Load       - Load knapsack data from file")
    print("Run        - Run algorithms and compare")
    print("Exit       - Exit the program (same as Ctrl+C)")

def process_command(command):
    args = command.split()
    cmd = args[0].lower()

    if cmd == 'help':
        display_help()
    elif cmd == 'generate':
        n = int(input('Number of items: '))
        C = int(input('Capacity of knapsack: '))
        filename = input('Output file name: ')
        generate_knapsack_data(filename, n, C)
        print(f"Data generated and saved to {filename}")
    elif cmd == 'load':
        filename = input('File name to load data from: ')
        global data
        data['C'], data['n'], data['values'], data['weights'] = load_knapsack_data(filename)
        print(f"Data loaded from {filename}")
    elif cmd == 'run':
        if 'C' in data and 'n' in data and 'values' in data and 'weights' in data:
            time_dynamic, time_brute_force = measure_performance(data['C'], data['weights'], data['values'], data['n'])
            print(f"Dynamic programming time: {time_dynamic}")
            print(f"Brute force time: {time_brute_force}")
        else:
            print("Data not loaded. Use the 'Load' command first.")
    elif cmd == 'exit':
        print('Exiting...')
        sys.exit(0)
    else:
        print('Invalid command. Type "help" for a list of commands.')

def main():
    while True:
        try:
            command = input('\naction> ')
            process_command(command)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
