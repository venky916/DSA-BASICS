from collections import deque

# Queue Implementation using deque
queue = deque()

# Enqueue: Adding elements to the end of the queue
queue.append(10)  # Adds 10 to the end of the queue
queue.append(20)  # Adds 20 to the end of the queue
queue.append(30)  # Adds 30 to the end of the queue
print(queue)  # Output: deque([10, 20, 30])

# Dequeue from the Front
front_element = queue.popleft()  # Removes and returns the front element
print(front_element)  # Output: 10
print(queue)  # Output: deque([20, 30])

# Dequeue from the End using pop
end_element = queue.pop()  # Removes and returns the last element
print(end_element)  # Output: 30
print(queue)  # Output: deque([20])

# Append Left: Adding an element to the beginning of the queue
queue.appendleft(5)  # Adds 5 to the beginning of the queue
print(queue)  # Output: deque([5, 20])

# Checking the Front Element without Removing
if queue:
    front_element = queue[0]
    print(front_element)  # Output: 5

# Checking if the Queue is Empty
is_empty = len(queue) == 0
print(is_empty)  # Output: False

# Queue Size
queue_size = len(queue)
print(queue_size)  # Output: 2