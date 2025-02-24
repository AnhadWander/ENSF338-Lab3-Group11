import json
import time
import matplotlib.pyplot as plt

def load_array_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def binary_search(arr, target, first_mid_index):
    left, right = 0, len(arr) - 1
    mid = first_mid_index  

    if mid < left or mid > right:
        raise ValueError("Invalid first midpoint index")
    
    midpoints = [mid]  

    while left <= right:
        if arr[mid] == target:
            return mid, midpoints
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        mid = left + (right - left) // 2
        midpoints.append(mid)
    
    return -1, midpoints  

data_filename = "ex7data.json"
arr = load_array_from_json(data_filename)

tasks_filename = "ex7tasks.json"
targets = load_array_from_json(tasks_filename)

first_mid_index = 500000  

scatter_x = [] 
scatter_y = []  

for target in targets:
    _, midpoints = binary_search(arr, target, first_mid_index)
    for mid in midpoints:
        scatter_x.append(target)
        scatter_y.append(mid)

plt.figure(figsize=(10, 6))
plt.scatter(scatter_x, scatter_y, alpha=0.5)
plt.xlabel("Target Value")
plt.ylabel("Midpoint Selected")
plt.title("Binary Search Midpoint Selection for Each Target")
plt.grid(True)
plt.show()
