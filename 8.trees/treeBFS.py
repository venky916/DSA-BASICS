from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


# breath first search using dfs approach
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root==None:
        return []
        
    def dfs(self,root,level,res):
        if root==None:
            return 
        if len(res)==level:
            res.append([])

        res[level].append(root.val)

        dfs(root.left,level+1,res)
        dfs(root.right,level+1,res)

    res=[]
    dfs(root,0,res)
    return res

