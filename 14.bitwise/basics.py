# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1

# Counting Bits
def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1 # same as n // 2
    return count
    

# ith bit set or not n & (1<<i) !=0 or (n>>i) &1 !=0
# clear ith bit n &(~(1<<i) )
# toggle ith bit n^(1<<i)

# remove last set bit (right most) n = n&(n-1) 
# power of 2  n & (n-1) ==0
