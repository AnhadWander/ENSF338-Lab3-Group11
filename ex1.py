import sys
sys.setrecursionlimit(20000)

def merge(arr, low, mid, high):
    lft = arr[low:mid+1]
    rt = arr[mid+1:high+1]

    i = 0
    j = 0

    while i < len(lft) and j < len(rt): 
        if lft[i] <= rt[j]:
            arr[low] = lft[i]    
            i += 1              
        else:
            arr[low] = rt[j]
            j += 1
        low += 1   

    while i < len(lft):   
        arr[low] = lft[i]   
        i += 1
        low += 1

    while j < len(rt):  
        arr[low] = rt[j]  
        j += 1
        low += 1

def merge_sort(arr, low, high): 
    if low < high:
        mid = (low+high) // 2
        merge_sort(arr, low, mid)   
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)  
    return arr
