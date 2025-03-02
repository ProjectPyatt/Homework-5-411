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

# Function to generate a random array of integers
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Function to test both sorting algorithms and return their execution times
def test_sorting_algorithms():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    insertion_sort_times = []
    merge_sort_times = []
    
    for size in sizes:
        arr = generate_random_array(size)  # Generate random array for each size
        insertion_sort_times.append(insertion_sort(arr[:]))  # Copy array to keep original intact
        
        _, merge_sort_time = merge_sort(arr[:])  # Get only the time taken (ignore sorted array)
        merge_sort_times.append(merge_sort_time)
    
    return sizes, insertion_sort_times, merge_sort_times

# Function to plot the results using matplotlib and save the graph
def plot_results(sizes, insertion_sort_times, merge_sort_times):
    plt.plot(sizes, insertion_sort_times, label='Insertion Sort')  # Plot Insertion Sort times
    plt.plot(sizes, merge_sort_times, label='Merge Sort')  # Plot Merge Sort times
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Time Complexity Comparison: Insertion Sort vs Merge Sort')
    
    # Save the plot as a PNG image
    plt.savefig('sorting_graphs.png')
    print("Graph saved as sorting_graphs.png")


# Run the sorting algorithms and plot the results
sizes, insertion_sort_times, merge_sort_times = test_sorting_algorithms()
plot_results(sizes, insertion_sort_times, merge_sort_times)
