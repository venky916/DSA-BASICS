# the return type is either val or none, so we need to check every recursive call 
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    def inorder(root, k, state):
        if not root:
            return None
        
        # Visit left subtree
        left_result = inorder(root.left, k, count)
        if left_result is not None:
            return left_result
        
        # Increment the counter and check if it's the kth node
        count[0] += 1
        if count[0] == k:
            return root.val
        
        # Visit right subtree
        return inorder(root.right, k, count)

    count = [0]  # Use a list to keep the counter mutable
    return inorder(root, k, count)


# if different return type make a global variable in list type since int will be assumed as local variable in python
# this simplifies and we dont need to concern on return type
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    count = [0]
    result = [0]  # Store the result in a list to update it inside the function

    def inorder(node, k):
        if node is None or count[0] >= k:
            return
        inorder(node.left, k)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val  # Update the result when kth element is found
        inorder(node.right, k)

    inorder(root, k)
    return result[0]


# iterative solution its a little simple
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    n=0
    stack=[]
    curr=root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left

        curr=stack.pop()
        n+=1
        if n==k:
            return curr.val
        curr=curr.right

# while using class base then we  can directly use self and act as public variables similar to global ones
# since we are suing global variables we dont need to consider the return
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            if root:
                inorder(root.left)
                self.count-=1
                if self.count==0:
                    self.number=root.val
                    return 
                inorder(root.right)

        self.count=k
        self.number=None
        inorder(root)
        return self.number