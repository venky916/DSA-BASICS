# Array Basic Operations
arr = [1, 2, 3, 4, 5]

# Accessing Elements
element = arr[2]  # Access element at index 2
print(element)  # Output: 3

# Appending an Element
arr.append(6)  # Adds an element to the end of the list
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

# Inserting an Element at a Specific Index
arr.insert(2, 10)  # Inserts 10 at index 2
print(arr)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Removing an Element by Value
arr.remove(3)  # Removes the first occurrence of 3
print(arr)  # Output: [1, 2, 10, 4, 5, 6]

# Removing an Element by Index
removed_element = arr.pop(2)  # Removes and returns the element at index 2
print(removed_element)  # Output: 10
print(arr)  # Output: [1, 2, 4, 5, 6]

# Finding the Index of an Element
index_of_value = arr.index(5)  # Returns the index of the first occurrence of 5
print(index_of_value)  # Output: 3

# Sorting
arr.sort()  # Sorts the list in ascending order
print(arr)  # Output: [1, 2, 4, 5, 6]

arr.sort(reverse=True)  # Sorts the list in descending order
print(arr)  # Output: [6, 5, 4, 2, 1]

# Reversing
arr.reverse()  # Reverses the order of the list
print(arr)  # Output: [1, 2, 4, 5, 6]

# Counting Occurrences of an Element
count_of_value = arr.count(4)  # Returns the number of occurrences of 4 in the list
print(count_of_value)  # Output: 1

# Copying a List
arr_copy = arr.copy()  # Creates a shallow copy of the list
print(arr_copy)  # Output: [1, 2, 4, 5, 6]

# Length of the List
length = len(arr)  # Returns the number of elements in the list
print(length)  # Output: 5

# Minimum and Maximum Values
min_value = min(arr)  # Returns the minimum value in the list
print(min_value)  # Output: 1

max_value = max(arr)  # Returns the maximum value in the list
print(max_value)  # Output: 6

# Sum of Elements
total_sum = sum(arr)  # Returns the sum of all elements in the list
print(total_sum)  # Output: 18

# Sorting with Custom Key (e.g., Lambda for complex sorts)
arr.sort(key=lambda x: -x)  # Sorts based on a custom lambda function (example: in descending order)
print(arr)  # Output: [6, 5, 4, 2, 1]

# Extending a List
arr.extend([7, 8])  # Adds multiple elements to the end of the list
print(arr)  # Output: [6, 5, 4, 2, 1, 7, 8]

# Slicing
sliced_arr = arr[1:4]  # Extracts a portion of the list from index 1 to 3 (4 is exclusive)
print(sliced_arr)  # Output: [5, 4, 2]

# Finding Unique Elements
unique_elements = list(set(arr))  # Returns unique elements by converting to a set, then back to a list
print(unique_elements)  # Output (order may vary): [1, 2, 4, 5, 6, 7, 8]
