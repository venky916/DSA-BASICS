import heapq

def find_kth_largest(nums, k):
    # Step 1: Create a min-heap with the first 'k' elements of the array
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # O(k) to build the heap

    # Step 2: Iterate over the remaining elements
    for num in nums[k:]:
        # If the current number is larger than the smallest in the heap (the root)
        if num > min_heap[0]:
            # Replace the root with the current number
            heapq.heapreplace(min_heap, num)

    # The root of the heap is the kth largest element
    return min_heap[0]

# Example usage
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(arr, k))  # Output: 5


def find_kth_smallest(nums, k):
    # Step 1: Create a min-heap from the array
    heapq.heapify(nums)

    # Step 2: Pop k-1 elements from the heap
    for _ in range(k - 1):
        heapq.heappop(nums)

    # Step 3: The kth smallest element is now at the root of the heap
    return nums[0]

# Example usage
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_smallest(arr, k))  # Output: 2

# just other approaches below


import heapq

def k_largest_maxheap(nums, k):
    # Convert all values to negatives to simulate a max heap
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    # Extract k largest elements (in negated form, revert to positive)
    return [-heapq.heappop(max_heap) for _ in range(k)]

def k_largest_minheap(nums, k):
    # Build a min heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Process the remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:  # Only insert if the number is larger than the smallest
            heapq.heappop(min_heap)  # Remove the smallest
            heapq.heappush(min_heap, num)
    
    # Return the k largest elements
    return min_heap  

def k_largest(nums,k):
    return heap.nlargest(k,nums)



import heapq

def k_smallest_maxheap(nums, k):
    # Create a max heap of size k by negating the first k elements
    max_heap = [-num for num in nums[:k]]
    heapq.heapify(max_heap)
    
    # Process the rest of the numbers
    for num in nums[k:]:
        if -num > max_heap[0]:  # Compare with the largest of the smallest k
            heapq.heappop(max_heap)  # Remove the largest
            heapq.heappush(max_heap, -num)
    
    # Return k smallest elements in ascending order
    return [-x for x in max_heap]  # Revert negation

def k_smallest_minheap(nums, k):
    # Transform the list into a min-heap
    heapq.heapify(nums)
    # Pop the smallest elements k times
    return [heapq.heappop(nums) for _ in range(k)]

def k_smallest(nums,k):
    return heap.nsmallest(k,nums)