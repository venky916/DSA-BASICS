def height(root):
    if root is None:  # Base case
        return 0
    left_height = height(root.left)  # Recursive case for left subtree
    right_height = height(root.right)  # Recursive case for right subtree
    return 1 + max(left_height, right_height)  # Add 1 for the current node

def sum_of_nodes(root):
    if root is None:  # Base case
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)  # Recursive case

# Example
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sum_of_nodes(root))  # Output: 6

def is_balanced(root):
    if root is None:  # Base case
        return True

    def height_and_balance(node):
        if node is None:  # Base case
            return 0, True
        
        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)
        
        height = 1 + max(left_height, right_height)
        balanced = abs(left_height - right_height) <= 1
        
        return height, balanced and left_balanced and right_balanced

    _, balanced = height_and_balance(root)
    return balanced

def is_balance(root):
    if root == None:
        return 0
    lh = is_balance(root.left)

    if lh ==-1:
        return -1
    rh = is_balance(root.right)
    if rh ==-1:
        return -1
    
    if abs(lh -rh)>1:
        return -1
    else:
        return max(lh,rh)+1


# Example
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_balanced(root))  # Output: True


def lowest_common_ancestor(root, p, q):
    if root is None or root == p or root == q:  # Base case
        return root
    
    left = lowest_common_ancestor(root.left, p, q)  # Recursive case
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root  # LCA found
    if left :
        return left
    else:
        return  right  # Return the non-null value

# Example
root = TreeNode(3, TreeNode(5), TreeNode(1))
p = root.left  # Node with value 5
q = root.right  # Node with value 1
print(lowest_common_ancestor(root, p, q).val)  # Output: 3


def diameter(root):
    def height_and_diameter(node):
        if node is None:  # Base case
            return 0, 0
        
        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)
        
        height = 1 + max(left_height, right_height)
        diameter = max(left_height + right_height, left_diameter, right_diameter)
        
        return height, diameter

    _, dia = height_and_diameter(root)
    return dia

# with slight modification on height method with jus adding additional variable res we can find diameter 
res=0
def height(root):
    if root == None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)

    res = max(res,1+lh+rh)

    return max(lh+rh)+1


# Example
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(diameter(root))  # Output: 2
