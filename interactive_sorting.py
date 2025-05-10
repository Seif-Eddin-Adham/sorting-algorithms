from sorting_algorithms import quick_sort, merge_sort, insertion_sort, measure_time, generate_test_arrays
import time
import random
from typing import List, Callable
import matplotlib.pyplot as plt
import numpy as np

def get_user_array() -> List[int]:
    """Get array input from user."""
    while True:
        try:
            input_str = input("Enter numbers separated by spaces (e.g., '5 2 8 1 9'): ")
            return [int(x) for x in input_str.split()]
        except ValueError:
            print("Invalid input! Please enter numbers separated by spaces.")

def generate_case_array(size: int, case: str) -> List[int]:
    """Generate array based on selected case."""
    if case == "best":
        return list(range(1, size + 1))  # Already sorted
    elif case == "worst":
        return list(range(size, 0, -1))  # Reverse sorted
    else:  # average
        return [random.randint(1, 1000) for _ in range(size)]

def visualize_sorting_step(arr: List[int], step_num: int, algorithm: str):
    """Visualize the current state of the array during sorting."""
    plt.clf()
    plt.bar(range(len(arr)), arr)
    plt.title(f"{algorithm} - Step {step_num}")
    plt.pause(0.5)

def track_sorting_steps(sort_func: Callable, arr: List[int], algorithm: str) -> List[int]:
    """Track and visualize sorting steps."""
    steps = []
    step_count = 0
    
    def track_step(current_arr: List[int]):
        nonlocal step_count
        step_count += 1
        steps.append(current_arr.copy())
        visualize_sorting_step(current_arr, step_count, algorithm)
    
    # Create a wrapper function to track steps
    def step_tracking_sort(arr_to_sort: List[int]) -> List[int]:
        if algorithm == "Quick Sort":
            return quick_sort_with_steps(arr_to_sort, track_step)
        elif algorithm == "Merge Sort":
            return merge_sort_with_steps(arr_to_sort, track_step)
        else:  # Insertion Sort
            return insertion_sort_with_steps(arr_to_sort, track_step)
    
    result = step_tracking_sort(arr.copy())
    plt.close()
    return result

def quick_sort_with_steps(arr: List[int], track_step: Callable) -> List[int]:
    """Quick sort implementation with step tracking."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    track_step(left + middle + right)
    return quick_sort_with_steps(left, track_step) + middle + quick_sort_with_steps(right, track_step)

def merge_sort_with_steps(arr: List[int], track_step: Callable) -> List[int]:
    """Merge sort implementation with step tracking."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_with_steps(arr[:mid], track_step)
    right = merge_sort_with_steps(arr[mid:], track_step)
    
    result = merge(left, right)
    track_step(result)
    return result

def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays into a single sorted array."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort_with_steps(arr: List[int], track_step: Callable) -> List[int]:
    """Insertion sort implementation with step tracking."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        track_step(arr.copy())
    return arr

def analyze_time_complexity(algorithm: str, arr: List[int]) -> dict:
    """Analyze and explain time complexity for the given algorithm and array."""
    n = len(arr)
    
    # Theoretical complexities
    complexities = {
        "Quick Sort": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n²)",
            "explanation": {
                "best": "When pivot divides array into equal parts",
                "average": "When pivot divides array into roughly equal parts",
                "worst": "When array is already sorted or reverse sorted"
            }
        },
        "Merge Sort": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n log n)",
            "explanation": {
                "best": "Always divides array into equal parts",
                "average": "Always divides array into equal parts",
                "worst": "Always divides array into equal parts"
            }
        },
        "Insertion Sort": {
            "best": "O(n)",
            "average": "O(n²)",
            "worst": "O(n²)",
            "explanation": {
                "best": "When array is already sorted",
                "average": "When elements are randomly distributed",
                "worst": "When array is reverse sorted"
            }
        }
    }
    
    # Determine the case
    if arr == sorted(arr):
        case = "best"
    elif arr == sorted(arr, reverse=True):
        case = "worst"
    else:
        case = "average"
    
    # Calculate actual operations for the specific case
    operations = {
        "Quick Sort": {
            "best": n * (n.bit_length()),  # n log n
            "average": n * (n.bit_length()),
            "worst": n * n  # n²
        },
        "Merge Sort": {
            "best": n * (n.bit_length()),  # n log n
            "average": n * (n.bit_length()),
            "worst": n * (n.bit_length())
        },
        "Insertion Sort": {
            "best": n,  # n
            "average": n * n // 2,  # n²/2
            "worst": n * n  # n²
        }
    }
    
    # Get the theoretical complexity and explanation
    theoretical_complexity = complexities[algorithm][case]
    explanation = complexities[algorithm]["explanation"][case]
    estimated_operations = operations[algorithm][case]
    
    return {
        "algorithm": algorithm,
        "array_size": n,
        "time_complexity": theoretical_complexity,
        "case": case,
        "explanation": explanation,
        "estimated_operations": estimated_operations
    }

def main():
    print("Welcome to the Interactive Sorting Algorithm Visualizer!")
    print("\nChoose an option:")
    print("1. Enter array manually")
    print("2. Generate array for specific case")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        arr = get_user_array()
    else:
        size = int(input("Enter array size: "))
        print("\nChoose case:")
        print("1. Best case (already sorted)")
        print("2. Worst case (reverse sorted)")
        print("3. Average case (random)")
        case_choice = input("Enter your choice (1, 2, or 3): ")
        case_map = {"1": "best", "2": "worst", "3": "average"}
        arr = generate_case_array(size, case_map[case_choice])
    
    print("\nChoose sorting algorithm:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    print("3. Insertion Sort")
    algo_choice = input("Enter your choice (1, 2, or 3): ")
    algo_map = {"1": "Quick Sort", "2": "Merge Sort", "3": "Insertion Sort"}
    algorithm = algo_map[algo_choice]
    
    print(f"\nOriginal array: {arr}")
    
    # First measure pure sorting time without visualization
    start_time = time.time()
    if algorithm == "Quick Sort":
        pure_sorted = quick_sort(arr.copy())
    elif algorithm == "Merge Sort":
        pure_sorted = merge_sort(arr.copy())
    else:
        pure_sorted = insertion_sort(arr.copy())
    pure_sort_time = time.time() - start_time
    
    # Now perform sorting with visualization
    start_time = time.time()
    sorted_arr = track_sorting_steps(
        quick_sort if algorithm == "Quick Sort" else 
        merge_sort if algorithm == "Merge Sort" else 
        insertion_sort,
        arr,
        algorithm
    )
    total_time = time.time() - start_time
    
    # Analyze and display results
    complexity_analysis = analyze_time_complexity(algorithm, arr)
    print("\nSorting Results:")
    print(f"Algorithm: {algorithm}")
    print(f"Array size: {len(arr)}")
    print(f"Pure sorting time (without visualization): {pure_sort_time:.6f} seconds")
    print(f"Total time (with visualization): {total_time:.6f} seconds")
    print(f"Visualization overhead: {total_time - pure_sort_time:.6f} seconds")
    print(f"\nTime Complexity Analysis:")
    print(f"Theoretical complexity: {complexity_analysis['time_complexity']}")
    print(f"Case: {complexity_analysis['case']}")
    print(f"Explanation: {complexity_analysis['explanation']}")
    print(f"Estimated number of operations: {complexity_analysis['estimated_operations']:,}")
    print(f"\nSorted array: {sorted_arr}")

if __name__ == "__main__":
    main() 