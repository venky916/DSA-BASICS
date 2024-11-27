# Brute Force T.C =>O(2**n) S.C =>O(n)
def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)

# Memoization T.C =>O(n) S.c =>O(n)
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]

cache = {}
memoization(5,cache)


# for bottom-up approach always write the recurrence relation to solve it.
# T.C = O(n) S.C =O(n)
def dp(n):
    if n < 2:
        return n

    dp = [-1]*(n+1)
    dp[0] =0
    dp[1] =1
    i = 2

    while i<=n:
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]


# Dynamic Programming with no extra space
# T.C =O(n) S.C =O(1)
def dp_no_space(n):
    if n < 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]