# Circular Queue Example (Fixed-Size Queue)
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return value

# Usage of CircularQueue
circular_queue = CircularQueue(3)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)  # Queue becomes full here
print(circular_queue.dequeue())  # Output: 1

# Common Queue Algorithms

# 1. Level Order Traversal of a Binary Tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Binary Tree Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(level_order_traversal(root))  # Output: [1, 2, 3, 4, 5]

# 2. Implementing Stack Using Queues
class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.popleft() if self.queue1 else None

# Usage of StackUsingQueues
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

# 3. Moving Average from Data Stream
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)

# Usage of MovingAverage
moving_average = MovingAverage(3)
print(moving_average.next(1))  # Output: 1.0
print(moving_average.next(10)) # Output: 5.5
print(moving_average.next(3))  # Output: 4.666...
print(moving_average.next(5))  # Output: 6.0

# 6. Recent Counter (Leetcode Problem - Simulates request calls within a time window)
class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        # Remove all pings older than 3000ms from the queue
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# Usage of RecentCounter
recent_counter = RecentCounter()
print(recent_counter.ping(1))    # Output: 1
print(recent_counter.ping(100))  # Output: 2
print(recent_counter.ping(3001)) # Output: 3
print(recent_counter.ping(3002)) # Output: 3

def generate_binary_numbers(n):
    queue = ["1"]
    result = []

    for _ in range(n):
        binary = queue.pop(0)
        result.append(binary)
        queue.append(binary + "0")
        queue.append(binary + "1")

    return result

# Example
print(generate_binary_numbers(5))  # Output: ['1', '10', '11', '100', '101']

# sliding window in advanced 