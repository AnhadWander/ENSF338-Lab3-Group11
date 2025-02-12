import timeit
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def time_function(func, arr):
    timer = timeit.Timer(lambda: func(arr.copy()))
    return timer.timeit(number=1)

sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50]
bubble_sort_times_best = []
bubble_sort_times_worst = []
bubble_sort_times_avg = []
quick_sort_times_best = []
quick_sort_times_worst = []
quick_sort_times_avg = []

for size in sizes:
    best_case = list(range(size))  
    worst_case = list(range(size, 0, -1))  
    avg_case = [random.randint(0, 1000) for _ in range(size)]  

    bubble_sort_times_best.append(time_function(bubble_sort, best_case))
    bubble_sort_times_worst.append(time_function(bubble_sort, worst_case))
    bubble_sort_times_avg.append(time_function(bubble_sort, avg_case))

    quick_sort_times_best.append(time_function(quick_sort, best_case))
    quick_sort_times_worst.append(time_function(quick_sort, worst_case))
    quick_sort_times_avg.append(time_function(quick_sort, avg_case))


