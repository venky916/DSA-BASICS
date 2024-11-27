# this is dfs,
    # dfs is RECURSION (base case and what u are returning) (or use a for loop)
    # dfs do BACKTRACKING (we need additional dataStructure like array or dictionary)
    # dfs always dont forget needs VISITED(SET/MAP) 

# this is mostly used to find the brute force approach 

# ques =>count unique paths from topLeft to bottom right.A single path may only move along 0's and can't visit same cell more than once. can move four directions
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or 
        grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    # backtrack
    visit.remove((r, c))
    return count

# T.C = O(4 ** (r*c)) (4 => all 4 directions depending on question) 
# similar to backtracking one checking all possibilities =>4 * height of tree(depth from top left to bottom i.e=> r*c)

# T.C = can be O(r*c) if we are not doing the same dfs of each element more than once depending on Question T.c changes 
# S.C = O(r*c) // visited map/set