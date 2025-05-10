import time
import random
from typing import List, Tuple

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_func, arr: List[int]) -> float:
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def generate_test_arrays(size: int) -> Tuple[List[int], List[int], List[int]]:
    # Random array
    random_arr = [random.randint(1, 1000) for _ in range(size)]
    
    # Sorted array
    sorted_arr = sorted(random_arr)
    
    # Reverse sorted array
    reverse_sorted_arr = sorted(random_arr, reverse=True)
    
    return random_arr, sorted_arr, reverse_sorted_arr 