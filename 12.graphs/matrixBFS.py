# this is bfs
    # bfs uses queue 
    # in graph we always use a visited (set/map)
    # while (till queue) 
        # for loop length of queue
            # for for directions if necessary

# bfs is mainly to find shortest/minimum solution once since better T.C than DFS



# ques=>shortest path from top-left to right-bottom in the grid
from collections import deque

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or 
                    grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

# with using additional prams we can do it using only 1 for loop similar to dijkstra one
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0,0))
    visit.add((0, 0))

    while queue:
        r, c,length = queue.popleft()
        if r == ROWS - 1 and c == COLS - 1:
            return length

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in neighbors:
            if (min(r + dr, c + dc) < 0 or
                r + dr == ROWS or c + dc == COLS or
                (r + dr, c + dc) in visit or 
                grid[r + dr][c + dc] == 1):
                continue
            queue.append((r + dr, c + dc,length+1))
            visit.add((r + dr, c + dc))


# multi source bfs also important 
def orangesRotting(self, grid: List[List[int]]) -> int:
    row=len(grid)
    col=len(grid[0])
    q=deque()
    fresh=0
    time=0
    
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                fresh+=1
            if grid[i][j]==2:
                q.append((i,j))
                
    directions=[(0,1),(0,-1),(1,0),(-1,0)]

    while q and fresh:

        for i in range(len(q)):
            r,c=q.popleft()

            for dr,dc in directions:

                i=r+dr
                j=c+dc

                if (i<0 or i>=row or
                    j<0 or j>=col or
                    grid[i][j]!=1):
                    continue

                grid[i][j]=2
                fresh-=1
                q.append((i,j))
            
        time+=1

    return time if fresh==0 else -1



# T.C =>O(r*c)
#  we only visited each element twice adding in to queue and popping out of queue 2*length of grid (2*r*c)
# S.C => O(r*c) visited set/Map