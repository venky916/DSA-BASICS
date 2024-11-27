# this is bfs
    # bfs uses queue 
    # in graph we always use a visited (set/map)
    # while (till queue) 
        # for loop length of queue
            # for for neighbors if necessary

# bfs is mainly to find shortest/minimum solution once since better T.C than DFS

from collections import defaultdict
from collections import deque

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adj=defaultdict(list)

for src,dst in edges:
    adj[src].append(dst)

#ques=> Shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length

# T.C =>O(V+E)
#  we only visited each node twice adding in to queue and popping out of queue 
# S.C => O(V+E) visited set/Map