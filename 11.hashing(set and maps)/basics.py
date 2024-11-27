names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    # If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1


# main question where can we use hashing
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic={}

    for i in range(len(nums)):
        compl=target-nums[i]
        if compl in dic:
            return [i,dic[compl]]
        dic[nums[i]]=i