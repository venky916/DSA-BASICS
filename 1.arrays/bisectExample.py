import bisect

# Sample sorted array
sorted_arr = [1, 3, 3, 5, 7, 9]

# bisect_left: Finds the insertion point for value to keep sorted_arr sorted (returns index of the first occurrence of value)
index_left = bisect.bisect_left(sorted_arr, 3)  # Returns index 1 (first occurrence of 3)
print(index_left)  # Output: 1

# bisect_right: Similar to bisect_left but returns index after the last occurrence of value
index_right = bisect.bisect_right(sorted_arr, 3)  # Returns index 3 (right after last occurrence of 3)
print(index_right)  # Output: 3

# bisect (alias of bisect_right): Returns insertion point after last occurrence of value
index_bisect = bisect.bisect(sorted_arr, 5)  # Returns index 4
print(index_bisect)  # Output: 4

# insort_left: Inserts value in sorted_arr at the position given by bisect_left, maintaining sorted order
bisect.insort_left(sorted_arr, 4)  # sorted_arr becomes [1, 3, 3, 4, 5, 7, 9]
print(sorted_arr)  # Output: [1, 3, 3, 4, 5, 7, 9]

# insort_right: Inserts value in sorted_arr at the position given by bisect_right, maintaining sorted order
bisect.insort_right(sorted_arr, 4)  # sorted_arr becomes [1, 3, 3, 4, 4, 5, 7, 9]
print(sorted_arr)  # Output: [1, 3, 3, 4, 4, 5, 7, 9]
