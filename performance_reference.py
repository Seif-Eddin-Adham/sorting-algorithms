from sorting_algorithms import quick_sort, merge_sort, insertion_sort, measure_time, generate_test_arrays
import matplotlib.pyplot as plt
import numpy as np

def analyze_performance():
    # Test sizes to analyze
    sizes = [100, 500, 1000, 5000, 10000]
    
    # Dictionary to store results
    results = {
        'quick_sort': {'random': [], 'sorted': [], 'reverse': []},
        'merge_sort': {'random': [], 'sorted': [], 'reverse': []},
        'insertion_sort': {'random': [], 'sorted': [], 'reverse': []}
    }
    
    # Run tests for each size
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        
        # Generate test arrays
        random_arr, sorted_arr, reverse_arr = generate_test_arrays(size)
        
        # Test each sorting algorithm
        for sort_name, sort_func in [
            ('quick_sort', quick_sort),
            ('merge_sort', merge_sort),
            ('insertion_sort', insertion_sort)
        ]:
            # Test random array
            time_random = measure_time(sort_func, random_arr)
            results[sort_name]['random'].append(time_random)
            
            # Test sorted array
            time_sorted = measure_time(sort_func, sorted_arr)
            results[sort_name]['sorted'].append(time_sorted)
            
            # Test reverse sorted array
            time_reverse = measure_time(sort_func, reverse_arr)
            results[sort_name]['reverse'].append(time_reverse)
            
            print(f"{sort_name}:")
            print(f"  Random array: {time_random:.6f} seconds")
            print(f"  Sorted array: {time_sorted:.6f} seconds")
            print(f"  Reverse sorted array: {time_reverse:.6f} seconds")
    
    # Plot results
    plot_results(sizes, results)

def plot_results(sizes, results):
    plt.figure(figsize=(15, 10))
    
    # Plot for random arrays
    plt.subplot(3, 1, 1)
    for sort_name in results:
        plt.plot(sizes, results[sort_name]['random'], marker='o', label=sort_name)
    plt.title('Performance on Random Arrays')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    # Plot for sorted arrays
    plt.subplot(3, 1, 2)
    for sort_name in results:
        plt.plot(sizes, results[sort_name]['sorted'], marker='o', label=sort_name)
    plt.title('Performance on Sorted Arrays')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    # Plot for reverse sorted arrays
    plt.subplot(3, 1, 3)
    for sort_name in results:
        plt.plot(sizes, results[sort_name]['reverse'], marker='o', label=sort_name)
    plt.title('Performance on Reverse Sorted Arrays')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('performance_reference.png')
    plt.close()

if __name__ == "__main__":
    print("Starting performance analysis...")
    analyze_performance()
    print("\nAnalysis complete! Results have been saved to 'performance_reference.png'") 