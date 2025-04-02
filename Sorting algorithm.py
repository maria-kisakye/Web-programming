import time#used to measure the execution time of sorting algorithms.
import random#generates random arrays for testing
import heapq#provides heap-related operations for heapsort

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]# elements smaller than the pivot
    middle = [x for x in arr if x == pivot]# elements equal to the pivot
    right = [x for x in arr if x > pivot]# elements greater than the pivot
    return quicksort(left) + middle + quicksort(right)

# Mergesort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []#This will store the merged sorted array.
    i = j = 0# pointers to the left and right arrays
    #compare elements from the left and right arrays and add the smaller one to the result array.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:#if the element in the left array is smaller
            result.append(left[i])#add it to the result array
            i += 1#move the pointer to the next element in the left array
        else:# otherwise, the cureent element in the right array is smaller or equal:
            result.append(right[j])# add it to the result array
            j += 1#Move the pointer in right array to the next element
    # Add any remaining elements from `left` (if `right` is exhausted).
    result.extend(left[i:])
    # Add any remaining elements from `right` (if `left` is exhausted).
    result.extend(right[j:])
    
    return result# Return the merged sorted array.

# Heapsort
def heapsort(arr):
    heapq.heapify(arr)  # Convert the array into a min-heap.
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Function to test sorting times
def test_sorting():#Defines a list of array sizes(1000,10000,100000) to test the sorting algorithms
    sizes = [1000, 10000, 100000]
    for size in sizes:# Generate a random array of integers between 0 and 100000 for each size
        arr = [random.randint(0, 100000) for _ in range(size)]
        print(f"\nSorting {size} elements:")#Print size of the array
        
        for sort_func, name in [(quicksort, 'Quicksort'), (mergesort, 'Mergesort'), (heapsort, 'Heapsort')]:# Test each sorting algorithm
            arr_copy = arr[:]
            start = time.time()# Measure the execution time of the sorting algorithm
            sort_func(arr_copy)
            end = time.time()
            print(f"{name}: {end - start:.6f} seconds")# Print the name of the sorting algorithm and the time it took to sort the array

# Run sorting tests
if __name__ == "__main__":
    test_sorting()#Call the test_sorting function to test the sorting algorithms
