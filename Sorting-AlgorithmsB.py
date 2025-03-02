import time
import random
import matplotlib.pyplot as plt

# Insertion Sort implementation
def insertion_sort(arr):
    start_time = time.time()  # Track start time
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()  # Track end time
    return end_time - start_time  # Return the time taken

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  # Base case: return array and 0 time

    start_time = time.time()  # Track start time

    mid = len(arr) // 2  # Find the middle index
    left_sorted, left_time = merge_sort(arr[:mid])  # Recursively sort the left half
    right_sorted, right_time = merge_sort(arr[mid:])  # Recursively sort the right half

    merged = merge(left_sorted, right_sorted)  # Merge the sorted halves

    end_time = time.time()  # Track end time
    total_time = (end_time - start_time) + left_time + right_time  # Sum recursive call times

    return merged, total_time  # Return the merged array and the total time taken

# Merge helper function for Merge Sort
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Append remaining elements from left
    result.extend(right[j:])  # Append remaining elements from right
    return result

# Function to generate a sorted array
def generate_sorted_array(size):
    return list(range(size))  # Creates a sorted list from 0 to size-1

# Function to test sorting algorithms on sorted lists
def test_sorting_algorithms_sorted():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    insertion_sort_times_sorted = []
    merge_sort_times_sorted = []
    
    for size in sizes:
        arr = generate_sorted_array(size)  # Generate sorted array for each size
        insertion_sort_times_sorted.append(insertion_sort(arr[:]))  # Copy to preserve original order
        
        _, merge_sort_time = merge_sort(arr[:])  # Get only the time taken (ignore sorted array)
        merge_sort_times_sorted.append(merge_sort_time)
    
    return sizes, insertion_sort_times_sorted, merge_sort_times_sorted

# Function to plot results for sorted lists and save the graph
def plot_sorted_results(sizes, insertion_sort_times_sorted, merge_sort_times_sorted):
    plt.plot(sizes, insertion_sort_times_sorted, label='Insertion Sort (Sorted Data)', linestyle='dashed')
    plt.plot(sizes, merge_sort_times_sorted, label='Merge Sort (Sorted Data)', linestyle='dashed')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Time Complexity (Sorted Lists): Insertion Sort vs Merge Sort')
    
    # Save the plot as a PNG image
    plt.savefig('sorted_sorting_graphs.png')
    print("Graph saved as sorted_sorting_graphs.png")

# Run the experiment on sorted lists
sizes, insertion_sort_times_sorted, merge_sort_times_sorted = test_sorting_algorithms_sorted()
plot_sorted_results(sizes, insertion_sort_times_sorted, merge_sort_times_sorted)