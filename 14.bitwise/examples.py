def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(10))  # Output: False

def count_ones(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Example
print(count_ones(15))  # Output: 4 (binary: 1111)
print(count_ones(7))   # Output: 3 (binary: 111)

def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example
arr = [2, 3, 2, 4, 4]
print(single_number(arr))  # Output: 3

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example
a, b = 5, 10
a, b = swap(a, b)
print(a, b)  # Output: 10, 5

def find_two_non_repeating(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num

    # Find rightmost set bit
    set_bit = xor_all & -xor_all

    x, y = 0, 0
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    return x, y

# Example
arr = [2, 4, 7, 9, 2, 4]
print(find_two_non_repeating(arr))  # Output: (7, 9)

def subsets(arr):
    n = len(arr)
    result = []
    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if bit i is set
                subset.append(arr[i])
        result.append(subset)
    return result

# Example
arr = [1, 2, 3]
print(subsets(arr))  
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def missing_number(arr, n):
    xor_all = 0
    xor_arr = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in arr:
        xor_arr ^= num
    return xor_all ^ xor_arr

# Example
arr = [1, 2, 4, 5, 6]
n = 6
print(missing_number(arr, n))  # Output: 3

def rightmost_set_bit(n):
    return n & -n

# Example
print(rightmost_set_bit(10))  # Output: 2 (binary: 1010 -> rightmost set bit: 0010)

def count_bits_to_convert(a, b):
    # ans
    xor = a ^ b 
    # result is no. of set bits in ans 
    count = 0
    while xor:
        xor &= (xor - 1)
        count += 1
    return count

# Example
print(count_bits_to_convert(29, 15))  # Output: 2

