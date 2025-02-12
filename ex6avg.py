import random
import time
import matplotlib.pyplot as plt
import numpy as np

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def measure_time(n, trials=100):
    lin_times = []
    bin_times = []

    for _ in range(trials):
        arr = [random.randint(0, 1000000) for _ in range(n)]
        target = arr[0]  
        random.shuffle(arr) 

        start = time.perf_counter()
        linear_search(arr, target)
        lin_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        sorted_arr = arr.copy()
        quicksort(sorted_arr, 0, len(sorted_arr) - 1)
        binary_search(sorted_arr, target)
        bin_times.append(time.perf_counter() - start)

    return np.mean(lin_times), np.mean(bin_times)

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
lin_results = []
bin_results = []

for size in sizes:
    lin_time, bin_time = measure_time(size)
    lin_results.append(lin_time)
    bin_results.append(bin_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, lin_results, label="Linear Search", marker="o")
plt.plot(sizes, bin_results, label="Quicksort + Binary Search", marker="s")
plt.xlabel("Input Size")
plt.ylabel("Avg Time (seconds)")
plt.title("Linear Search vs Binary Search (with Quicksort)")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()


# For small inputs (n ≤ 100):
# Linear search is faster because sorting overhead makes quicksort + binary search slower.

# For medium inputs (n ≈ 200 - 500):
# Performance is similar, with binary search starting to become faster.

# For large inputs (n > 1000):
# Binary search (with quicksort) is much faster as sorting cost amortizes over multiple searches.