# 5. Finding Next Greater Element
def next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

print(next_greater_elements([2, 1, 2, 4, 3]))  # Output: [4, 2, 4, -1, -1]

def prev_greater_element(arr):
    # Initialize an empty stack and the result array
    stack = []
    result = []
    
    # Traverse the array from left to right
    for num in arr:
        # Pop elements from the stack that are less than or equal to the current number
        while stack and stack[-1] <= num:
            stack.pop()
        
        # If the stack is not empty, the top element is the previous greater element
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        
        # Push the current number onto the stack
        stack.append(num)
    
    return result

# Example usage
arr = [4, 5, 2, 10, 8]
result = prev_greater_element(arr)
print("Previous Greater Elements:", result)  # Output: [-1, 4, 5, -1, 10]

# the number of consecutive days including the current one for which the elements are smaller or equal to the current element
# (index of current element - index of closest greater element on leftSide )+1
def stock_span(prices):
    stack = []
    span = []

    for i, price in enumerate(prices):
        days = 1
        while stack and stack[-1][0] <= price:
            days += stack.pop()[1]
        stack.append((price, days))
        span.append(days)

    return span

# Example
prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))  # Output: [1, 1, 1, 2, 1, 4, 6]