# SEARCH RANGES 3 VARIATIONS AND THERE DIFFERENCE

# when l<=r we need to use extra variable for answer
def firstBadVersion(self, n: int) -> int:
    l=1
    r=n
    ans=r

    while l<=r:
        mid=(l+r)//2
        guess = isBadVersion(mid)

        if guess ==False:
            l=mid+1
        else:
            ans= min(ans,mid)
            r=mid-1
    return ans



# when l<r we might r=mid or l=mid we have to assign
def firstBadVersion(self, n: int) -> int:
    l=1
    r=n
    while l<r:
        mid=(l+r)//2
        guess = isBadVersion(mid)

        if guess ==False:
            l=mid+1
        else:
            r=mid
    return l
            

# if we dont assign like that,then we need to make a additional check
def firstBadVersion(self, n: int) -> int:
    l=1
    r=n

    while l<=r:
        mid=(l+r)//2
        guess = isBadVersion(mid)

        if guess ==False:
            l=mid+1
        else:
            if isBadVersion(mid-1) == False:
                return mid
            else:
                r= mid-1
    return False        
                        