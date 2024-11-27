# Binary search on some range of values
def binarySearch(low, high):
    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1

# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0

# maximum in minimum or minimum of maximum always uses binary search range approach over dp 
def is_feasible(pages, k, max_pages):
    # Function to check if it's possible to assign books such that
    # no student reads more than max_pages
    students_needed = 1  # Start with one student
    current_sum = 0

    for page in pages:
        current_sum += page
        if current_sum > max_pages:
            students_needed += 1
            current_sum = page
            if students_needed > k:  # More students are required than available
                return False
    return True

def min_pages(pages, k):
    # Binary Search for the answer
    low = max(pages)  # Minimum possible max_pages is the largest single book
    high = sum(pages)  # Maximum possible max_pages is the sum of all pages

    result = high
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(pages, k, mid):
            result = mid  # We can try to minimize the max pages
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# Example usage
pages = [12, 34, 67, 90]
k = 2
print("Minimum of the maximum pages:", min_pages(pages, k))  # Output: 113
