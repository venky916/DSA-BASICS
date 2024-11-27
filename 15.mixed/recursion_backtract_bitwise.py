def print_subsets(s, idx=0, curr=[]):
    if idx == len(s):  # Base case
        print(curr)
        return
    print_subsets(s, idx + 1, curr)  # Recursive case without including s[idx]
    print_subsets(s, idx + 1, curr + [s[idx]])  # Recursive case including s[idx]

# Example
print_subsets([1, 2, 3])

def subsets(self, nums: List[int]) -> List[List[int]]:

    def help(i,n,sub,res):
        if i==n:
            res.append(sub.copy())
            return
        
        # adding in the element,including the ith element
        sub.append(nums[i])
        help(i+1,n,sub,res)

        # backtracking remove the added one , not including ith element
        sub.pop()
        help(i+1,n,sub,res)

    sub=[]
    res=[]
    n=len(nums)
    help(0,n,sub,res)
    
    return res

def subsets(arr):
    n = len(arr)
    result = []
    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if bit i is set
                subset.append(arr[i])
        result.append(subset)
    return result

# Example
arr = [1, 2, 3]
print(subsets(arr))  
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


def subsets(nums):
    result=[[]]

    for val in nums:
        curr=[]
        for subset in result:
            curr +=[subset +[val]]
        result+=curr
        
    return result

# always prefer the dfs approach during finding all possibilities one