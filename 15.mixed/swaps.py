def swap_using_xor(a, b):
    # Step 1: XOR a and b and assign it to a
    a = a ^ b

    # Step 2: XOR a and b and assign it to b
    b = a ^ b

    # Step 3: XOR a and b and assign it to a
    a = a ^ b

    return a, b

# Example usage:
a, b = 5, 10
a, b = swap_using_xor(a, b)
print("a:", a, "b:", b)  # Output: a: 10 b: 5


def swap_using_temp_variable(a, b):
    # Step 1: Use a temporary variable to hold one value
    temp = a

    # Step 2: Assign the second value to the first
    a = b

    # Step 3: Assign the temporary variable (the original value of a) to b
    b = temp

    return a, b

# Example usage:
a, b = 5, 10
a, b = swap_using_temp_variable(a, b)
print("a:", a, "b:", b)  # Output: a: 10 b: 5


def swap_using_addition_subtraction(a, b):
    # Step 1: Add both numbers and store the sum in a
    a = a + b

    # Step 2: Subtract the new value of a (which is a + b) from b to get the original a
    b = a - b

    # Step 3: Subtract the new value of b (which is original a) from a to get the original b
    a = a - b

    return a, b

# Example usage:
a, b = 5, 10
a, b = swap_using_addition_subtraction(a, b)
print("a:", a, "b:", b)  # Output: a: 10 b: 5
