# this is dfs,
    # dfs is RECURSION (base case and what u are returning) (or use a for loop)
    # dfs do BACKTRACKING (we need additional dataStructure like array or dictionary)
    # dfs always dont forget needs VISITED(SET/MAP) the additional data structure
    # here we need to use for loop for all its adjacent neighbors

# this is mostly used to find the brute force approach

# ques => count paths from src to target

from collections import defaultdict

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adj=defaultdict(list)

for src,dst in edges:
    adj[src].append(dst)
    # adj[dst].append(src) //if undirected we add this also


# Count paths (backtracking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count

# T.C => generally for all possible approach since ist backtracking which is brute force
# T.c is if we are  visiting same node more than once and trying all possible ways O(v**E)
# T.C if we are visiting each node once the O(V+E)

# S.C => O(V+E)