import timeit
import random
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def benchmark_sorting(scenario, array_sizes):
    times = []
    for n in array_sizes:
        if scenario == 'best':
            arr = list(range(n))
        elif scenario == 'worst':
            arr = list(range(n, 0, -1))
        elif scenario == 'average':
            arr = [random.randint(1, 1000) for _ in range(n)]

        time_taken = timeit.timeit(lambda: quicksort(arr[:]), number=1)
        times.append(time_taken)
    return times

# Benchmark configurations
array_sizes = [100, 500, 1000, 2000, 5000]
scenarios = ['best', 'worst', 'average']

# Benchmarking
results = {scenario: [benchmark_sorting(scenario, array_sizes) for _ in range(5)] for scenario in scenarios}

# Plotting
plt.figure(figsize=(10, 6))
for scenario, times_list in results.items():
    avg_times = [sum(times) / len(times) for times in zip(*times_list)]
    plt.plot(array_sizes, avg_times, label=scenario)

plt.title('Quicksort Performance Comparison (Non-Random Pivot)')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
