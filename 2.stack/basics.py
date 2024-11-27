# Stack Implementation using a List
stack = []

# Pushing an Element onto the Stack
stack.append(10)  # Adds 10 to the top of the stack
stack.append(20)  # Adds 20 to the top of the stack
print(stack)  # Output: [10, 20]

# Popping an Element from the Stack
top_element = stack.pop()  # Removes and returns the top element
print(top_element)  # Output: 20
print(stack)  # Output: [10]

# Checking the Top Element without Removing
if stack:
    top_element = stack[-1]
    print(top_element)  # Output: 10

# Checking if the Stack is Empty
is_empty = len(stack) == 0
print(is_empty)  # Output: False

# Stack Size
stack_size = len(stack)
print(stack_size)  # Output: 1