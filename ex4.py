import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(20000)
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

sizes = [1, 2, 4, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]
times = []

for n in sizes:
    arr = list(range(1, n+1))  
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    times.append(end_time - start_time)
    print(f"n = {n}, Time = {end_time - start_time:.6f} seconds")

    
plt.figure(figsize=(8, 6))
plt.plot(sizes, times, 'bo-', label="Quicksort Time")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Quicksort Worst-Case Complexity")

fit = np.polyfit(sizes, times, 2)
quadratic_fit = np.poly1d(fit)
x_values = np.linspace(min(sizes), max(sizes), 100)
plt.plot(x_values, quadratic_fit(x_values), 'r--', label="Quadratic Fit")

plt.legend()
plt.grid()
plt.show()