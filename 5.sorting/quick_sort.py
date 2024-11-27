# hoare's partition, pivot  is first 
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end

    while True:
        # Move i to the right while arr[i] <= pivot
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
        
        # Move j to the left while arr[j] > pivot
        while arr[j] > arr[pivot]:
            j -= 1

        # If i < j, swap the elements, otherwise, break the loop
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break  # Break when i >= j

    # Swap the pivot into the correct position
    arr[start], arr[j] = arr[j], arr[start]

    # Recursively sort the two halves
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)


# lamuto partion all use lamuto while using dsa
# many dsa problem used using lamuto only , pivot is last
def quick_sort_2(arr, start, end):
    if end - start + 1 <= 1:  
        return

    pivot = arr[end]  # Choose pivot as the last element
    index = start  # Initialize index for swapping elements smaller than pivot

    for i in range(start, end):  # Loop over the array (excluding the pivot)
        if arr[i] <= pivot:  # If the current element is less than pivot
            arr[index], arr[i] = arr[i], arr[index]  # Swap the elements
            index += 1  # Move the index to the next element smaller than pivot

    # Place the pivot in its correct position
    arr[index], arr[end] = arr[end], arr[index]

    # Recursively apply quick_sort to the left and right partitions
    quick_sort_2(arr, start, index)
    quick_sort_2(arr, index + 1, end)

        
