# actually this is counting sort
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


# actual bucket sort
def bucket_sort(arr,n,k):
    max_val= max(arr)
    max_val+=1

    bkt=[[]*k]

    for i in range(n):
        bi=(k*arr[i])//max_val
        bkt[bi].append(arr[i])
    
    for i in range(k):
        bkt[i].sort()
    
    index=0
    for i in range(k):
        for j in range(len(bkt[i])):
            arr[index]=bkt[i][j]
            index+=1