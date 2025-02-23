import timeit
import random
import matplotlib.pyplot as plt

def traditional_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i - 1)
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key
    return arr

def random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def run_experiment(algrthm, sizes):
    results = []
    for size in sizes:
        arr = random_array(size)
        time_taken = timeit.timeit(lambda: algrthm(arr), number=1)
        results.append(time_taken)
    return results

# Input sizes to test
sizes = [100, 500, 1000, 5000, 10000]

# Run experiments
traditional_results = run_experiment(traditional_insertion, sizes)
binary_results = run_experiment(binary_insertion, sizes)

plt.figure(figsize=(10, 10))

# Traditional Insertion Sort
plt.plot(sizes, traditional_results, label="Traditional Insertion Sort")

# Binary Insertion Sort
plt.plot(sizes, binary_results, label="Binary Insertion Sort")

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Traditional vs Binary Insertion Sort")
plt.legend()
plt.savefig("Results.jpg")

'''
4. Discuss the results: which algorithm is faster? Why?

Binary Inserting Sort algorithm is faster as compared to the traditional insertion sort because it uses binary search
for comparisons instead of the linear search used by the traditional insertion sort and this reduces the total number
of comparisons done by the algorithm to make swaps.

'''