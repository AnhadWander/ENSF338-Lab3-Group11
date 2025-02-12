import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1  
            if arr[j] > arr[j + 1]:
                swaps += 1  
                temp = arr[j]        
                arr[j] = arr[j + 1] 
                arr[j + 1] = temp  
    return comparisons, swaps


def random_input(s):
    return [random.randint(1, 1000) for j in range(s)]


inpt_sizes = [25, 50, 100, 200, 500]
comparisons_list = []
swaps_list = [] 

for i in inpt_sizes:
    arr = random_input(i)
    print(f'Input size: {i}')
    print('-'*130)
    print('Original array:', arr)  
    print('-'*130)
    comparisons, swaps = bubble_sort(arr)
    comparisons_list.append(comparisons)
    swaps_list.append(swaps)
    print('Sorted array:', arr) 
    print('-'*130) 
    print(f'Comparisons: {comparisons}')
    print('-'*130)
    print(f'Swaps: {swaps}')
    print('*'*130)


def comparisons(n):
    return n * (n - 1) / 2

def swaps(n):
    return n * (n - 1) / 4

plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1)
plt.plot(inpt_sizes, comparisons_list, 'g', label="Comparisons")
plt.plot(inpt_sizes, [comparisons(n) for n in inpt_sizes], 'r:', label="Comparisons (Expected)")
plt.title("Number of Comparisons vs Input Size")
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(inpt_sizes, swaps_list, 'g', label="Swaps")
plt.plot(inpt_sizes, [swaps(n) for n in inpt_sizes], 'r:', label="Swaps (Expected)")
plt.title("Number of Swaps vs Input Size")
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Swaps")
plt.legend()

plt.savefig("Plots")
