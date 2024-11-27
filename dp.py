def count_factors(num, factor):
    """Counts how many times `factor` divides `num`."""
    count = 0
    while num % factor == 0 and num > 0:
        num //= factor
        count += 1
    return count

def solve(n, tiles):
    # Initialize DP tables for factors of 2 and 5
    dp2 = [[float('inf')] * n for _ in range(n)]
    dp5 = [[float('inf')] * n for _ in range(n)]
    
    # Base case
    dp2[0][0] = count_factors(tiles[0][0], 2)
    dp5[0][0] = count_factors(tiles[0][0], 5)
    
    # Fill the DP tables (using your top and left idea)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            factors_2 = count_factors(tiles[i][j], 2)
            factors_5 = count_factors(tiles[i][j], 5)
            
            # Take the minimum from top or left
            if i > 0:
                dp2[i][j] = min(dp2[i][j], dp2[i-1][j] + factors_2)
                dp5[i][j] = min(dp5[i][j], dp5[i-1][j] + factors_5)
            if j > 0:
                dp2[i][j] = min(dp2[i][j], dp2[i][j-1] + factors_2)
                dp5[i][j] = min(dp5[i][j], dp5[i][j-1] + factors_5)
    
    # The result is the minimum of the two values at the bottom-right corner
    return min(dp2[n-1][n-1], dp5[n-1][n-1])


def count_factors(num):
    """Counts how many times `factor` divides `num`."""
    count = 0
    while num % 10 == 0 and num > 0:
        num //= 10
        count += 1
    return count

def solve(n, tiles):
    dp_mul = [[float('inf')] * n for _ in range(n)]
    dp_cnt = [[float('inf')] * n for _ in range(n)]
    
    # Base case
    dp_mul[0][0] = tiles[0][0]
    dp_cnt[0][0] = count_factors(tiles[0][0])
    
    # Fill the DP tables (using your top and left idea)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            # Take the minimum from top or left
            if i > 0:
                top = dp_mul[i-1][j] * tiles[i][j]
                top_cnt = count_factors(top)
                if dp_cnt[i][j] > top_cnt:
                    dp_mul[i][j] = top
                    dp_cnt[i][j] = top_cnt
            if j > 0:
                left = dp_mul[i][j-1] * tiles[i][j]
                left_cnt = count_factors(left)
                if dp_cnt[i][j] > left_cnt:
                    dp_mul[i][j] = left
                    dp_cnt[i][j] = left_cnt
    
    return dp_cnt[n-1][n-1]

def count_trailing_zeros(num):
    """Count the number of trailing zeros in a number."""
    count = 0
    while num % 10 == 0 and num > 0:
        num //= 10
        count += 1
    return count

def solve(n, tiles):
    # Initialize DP table to store the trailing zeros count
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Base case
    dp[0][0] = count_trailing_zeros(tiles[0][0])
    
    # Fill the DP table
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            # Current cell trailing zeros
            current_zeros = count_trailing_zeros(tiles[i][j])
            
            # Transition from the top
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + current_zeros)
            
            # Transition from the left
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + current_zeros)
    
    # Return the minimum trailing zeros count at the bottom-right
    return dp[n-1][n-1]
