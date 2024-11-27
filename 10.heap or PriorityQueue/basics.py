arr = [3, 1, 4, 1, 5, 9]
heapq.heapify(arr)
print(arr)  # Output will be a min-heap: [1, 1, 3, 4, 5, 9]

heap = [1, 3, 5, 7, 9]
heapq.heappush(heap, 2)
print(heap)  # Output will be: [1, 2, 5, 7, 9, 3]

heap = [1, 2, 5, 7, 9]
smallest = heapq.heappop(heap)
print(smallest)  # Output will be: 1
print(heap)      # Output will be: [2, 7, 5, 9]

heap = [1, 3, 5, 7, 9]
replaced = heapq.heapreplace(heap, 4)
print(replaced)  # Output will be: 1 (the element that was replaced)
print(heap)      # Output will be: [3, 4, 5, 7, 9]

heap = [1, 3, 5, 7, 9]
popped = heapq.heappushpop(heap, 0)
print(popped)  # Output will be: 0 (the element that was popped)
print(heap)    # Output will be: [1, 3, 5, 7, 9]            
        

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)  # Use negative values for max-heap

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None
   