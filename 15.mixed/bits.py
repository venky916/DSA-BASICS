# 00001101 to 00001101
def reverse_bits(n):
    result = 0
    for i in range(32):  # Assuming 32-bit integer
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example
n = 43261596  # Binary: 00000010100101000001111010011100
print(reverse_bits(n))  # Output: 964176192

def reverseBits(self, n: int) -> int:
    x=2**31
    ans=0

    while n:
        if n%2==1:
            ans+=x
        x=x//2
        n=n//2

    return ans

def reverseBits(self, n: int) -> int:
    ans=0

    for i in range(32):
        bit =(n>>i) & 1
        ans= ans | (bit<<31-i)
    
    return ans


def reverseBits(self, n: int) -> int:
    reversed_n=0

    for _ in range(32):
        reversed_n= reversed_n <<1
        reversed_n = reversed_n | (n &1)
        n=n>>1
    return reversed_n


# question =>Given an array of integers, the task is to find the maximum XOR value that can be obtained by XOR-ing any two numbers in the array.

# Approach in the Code:
# The algorithm uses a greedy bitwise approach:

# Iterating from the Most Significant Bit (MSB):
# Start from the 31st bit (assuming 32-bit integers) and move down to the 0th bit.
# For each bit position, determine whether it's possible to set the current bit in the XOR result to 1 while ensuring that such a pair of numbers exists in the array.

# Using a Mask to Isolate Prefixes:
# A mask is used to progressively include more significant bits as we move down from MSB to LSB. This allows us to focus only on the significant bits at each stage.

# Example: At bit position i, the mask might look like 11100000... for isolating the first 32-i bits.

# Using a Set for Prefixes:
# Compute the prefixes of all numbers in the array by applying the mask. These prefixes represent the numbers with only the most significant 32-i bits considered.
# Greedy XOR Maximization:

# Assume the current bit can be set to 1 in the XOR result, which would make the temporary result temp = max_xor_val | (1 << i).
# Check if there exists a pair of prefixes p1 and p2 such that:
# Copy code
# p1 ^ p2 = temp
# This is equivalent to:
# makefile
# Copy code
# p1 = p2 ^ temp
# If such a pair exists, it means we can set the current bit to 1.
# Update the Result:

# If the current bit can be set to 1, update the max_xor_val with temp.

def max_xor(arr):
    max_xor_val = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in arr}
        temp = max_xor_val | (1 << i)
        if any((prefix ^ temp) in prefixes for prefix in prefixes):
            max_xor_val = temp
    return max_xor_val

# Example
arr = [3, 10, 5, 25, 2, 8]
print(max_xor(arr))  # Output: 28