# Common Stack Algorithms

# 1. Balancing Parentheses
def is_balanced_parentheses(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0

print(is_balanced_parentheses("({[]})"))  # Output: True
print(is_balanced_parentheses("({[})"))   # Output: False

# 2. Reverse a String using Stack
def reverse_string(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print(reverse_string("hello"))  # Output: "olleh"

# 3. Implementing a Queue using Two Stacks (FIFO behavior)
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# 4. Evaluate Postfix Expression
def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Integer division for compatibility
    return stack.pop()

print(evaluate_postfix("231*+9-"))  # Output: -4