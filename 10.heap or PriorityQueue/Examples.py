import heapq

def merge_k_sorted_arrays(arrays):
    heap = []
    for i, array in enumerate(arrays):
        if array:  # Push the first element of each array
            heapq.heappush(heap, (array[0], i, 0))
    
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(arrays[i]):  # Push the next element from the same array
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))
    
    return result

# Example
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge_k_sorted_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


import heapq
# For a nearly sorted array with each element at most k positions away from its sorted position,
#  if we maintain a min-heap of size k+1, we can always ensure that the smallest element is at the root of the heap. 
# This allows us to insert and extract the minimum element efficiently.
# We can iterate through the array, pushing the elements into the heap,
#  and then pop from the heap to get the smallest element.
#  Once the heap is full, we pop the smallest element and continue this process.

def sort_nearly_sorted(arr, k):
    heap, result = [], []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
        if len(heap) > k:
            result.append(heapq.heappop(heap))
    while heap:
        result.append(heapq.heappop(heap))
    return result

# Example
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(sort_nearly_sorted(arr, k))  # Output: [2, 3, 5, 6, 8, 9, 10]


import heapq
# Given n ropes with different lengths, you need to connect all the ropes into one single rope.
#  The cost of connecting two ropes is the sum of their lengths.
#  The goal is to minimize the total cost required to connect all the ropes.
def minimize_cost(ropes):
    heapq.heapify(ropes)
    cost = 0

    while len(ropes) > 1:
        a = heapq.heappop(ropes)
        b = heapq.heappop(ropes)
        cost += a + b
        heapq.heappush(ropes, a + b)
    
    return cost

# Example
ropes = [4, 3, 2, 6]
print(minimize_cost(ropes))  # Output: 29
