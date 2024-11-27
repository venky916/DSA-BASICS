# for each element it can be in the set or it may not be 2 choices 
# 2 options thats the brute force na

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