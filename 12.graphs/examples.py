def count_connected_components(adj_list):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in adj_list:
        if node not in visited:
            count += 1
            dfs(node)
    return count

# Example
adj_list = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
print(count_connected_components(adj_list))  # Output: 3

# detect cycle
# dfs approach where its neighbor is not parent one then it has cycle

# for undirected visited set is enough
def has_cycle_undirected(adj_list, node, visited, parent):
    visited.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if has_cycle_undirected(adj_list, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False

def detect_cycle_undirected(adj_list):
    visited = set()
    for node in adj_list:
        if node not in visited:
            if has_cycle_undirected(adj_list, node, visited, -1):
                return True
    return False

# Example
adj_list = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
print(detect_cycle_undirected(adj_list))  # Output: True

# directed 
# for undirected visited set  
# we need to keep track of all its ancestor in rec_st set
def has_cycle_directed(adj_list, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if has_cycle_directed(adj_list, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True
    rec_stack.remove(node)
    return False

def detect_cycle_directed(adj_list):
    visited, rec_stack = set(), set()
    for node in adj_list:
        if node not in visited:
            if has_cycle_directed(adj_list, node, visited, rec_stack):
                return True
    return False

# Example
adj_list = {0: [1], 1: [2], 2: [0]}
print(detect_cycle_directed(adj_list))  # Output: True


def shortest_path_unweighted(adj_list, start, target):
    visited = set()
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in adj_list[node]:
                queue.append((neighbor, distance + 1))
    return -1

# Example
adj_list = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
print(shortest_path_unweighted(adj_list, 0, 2))  # Output: 2