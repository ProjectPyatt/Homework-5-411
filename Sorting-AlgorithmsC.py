import time
import random
import matplotlib.pyplot as plt

# Insertion Sort implementation
def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return end_time - start_time  # Return the time taken

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  # Base case

    start_time = time.time()
    mid = len(arr) // 2
    left_sorted, left_time = merge_sort(arr[:mid])
    right_sorted, right_time = merge_sort(arr[mid:])
    merged = merge(left_sorted, right_sorted)
    end_time = time.time()

    total_time = (end_time - start_time) + left_time + right_time
    return merged, total_time

# Merge helper function
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to generate a sorted array
def generate_sorted_array(size):
    return list(range(size))

# Function to introduce disorder by swapping elements
def introduce_disorder(arr, num_swaps):
    n = len(arr)
    for _ in range(num_swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]  # Swap two random elements
    return arr

# Function to determine when Merge Sort becomes faster
def test_disorder_threshold(fixed_size=5000):
    swap_counts = list(range(0, fixed_size + 1, fixed_size // 20))  # Vary disorder levels
    insertion_sort_times = []
    merge_sort_times = []

    for num_swaps in swap_counts:
        arr = generate_sorted_array(fixed_size)  # Start with a sorted array
        arr = introduce_disorder(arr, num_swaps)  # Introduce disorder

        insertion_sort_time = insertion_sort(arr[:])  # Copy to avoid modifying original
        _, merge_sort_time = merge_sort(arr[:])  # Copy to avoid modifying original

        insertion_sort_times.append(insertion_sort_time)
        merge_sort_times.append(merge_sort_time)

    return swap_counts, insertion_sort_times, merge_sort_times

# Function to plot the results
def plot_disorder_results(swap_counts, insertion_sort_times, merge_sort_times):
    plt.plot(swap_counts, insertion_sort_times, label="Insertion Sort")
    plt.plot(swap_counts, merge_sort_times, label="Merge Sort")
    plt.xlabel("Number of Out-of-Order Elements")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title("Disorder vs Sorting Time: Insertion vs Merge Sort")
    
    # Save the graph
    plt.savefig("disorder_threshold_graph.png")
    print("Graph saved as disorder_threshold_graph.png")

# Run the experiment and plot the results
swap_counts, insertion_sort_times, merge_sort_times = test_disorder_threshold()
plot_disorder_results(swap_counts, insertion_sort_times, merge_sort_times)
