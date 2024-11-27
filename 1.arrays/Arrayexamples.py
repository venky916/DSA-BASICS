def find_missing(arr, n):
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

# Example
arr = [1, 2, 4, 5, 6]  # Missing number is 3
n = 6
print(find_missing(arr, n))  # Output: 3

def find_duplicates(arr):
    seen, duplicates = set(), set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))  # Output: [2, 3]

def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]


def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(find_intersection(arr1, arr2))  # Output: [2]

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Example
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True

def move_zeroes(arr):
    non_zeroes = [num for num in arr if num != 0]
    return non_zeroes + [0] * (len(arr) - len(non_zeroes))

# Example
arr = [0, 1, 0, 3, 12]
print(move_zeroes(arr))  # Output: [1, 3, 12, 0, 0]
