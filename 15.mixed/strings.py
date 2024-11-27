# check string is subsequence
def is_subsequence(s1, s2):
    i, j = 0, 0
    
    # Traverse through s2
    while i < len(s1) and j < len(s2):
        # If characters match, move pointer for s1
        if s1[i] == s2[j]:
            i += 1
        # Always move pointer for s2
        j += 1
    
    # If we traversed the entirety of s1, it's a subsequence
    return i == len(s1)

def is_subsequence_recursive(s1,s2,n,m):
    if m==0:
        return True
    if n==0:
        return False
    
    if s1[n-1] == s2[m-1]:
        return is_subsequence_recursive(s1,s2,n-1,m-1)
    else:
        return is_subsequence_recursive(s1,s2,n-1,m)

# appraoch one
def leftmost_repeating_char(s):
    CHAR = 256  # Total possible ASCII characters
    count = [0] * CHAR  # Initialize the count array
    
    # Fill the count array with occurrences of each character
    for char in s:
        count[ord(char)] += 1

    # Find the leftmost repeating character
    for char in s:
        if count[ord(char)] > 1:
            return char
    
    return None  # No repeating character found

# Example usage
s = "geeksforgeeks"
result = leftmost_repeating_char(s)
print("Leftmost Repeating Character:", result)  # Output: g


def leftmost_repeating_char_2(s):
    CHAR = 256  # Total possible ASCII characters
    freq_index = [-1] * CHAR  # Initialize the count array
    
    res = float('inf')
    # storing index in array 
    for i in range(len(s)):
        fi = freq_index[ord(s[i])]
        if fi == -1:
            freq_index[ord(char)] = i
        else:
            res = min(res,fi)
    return res if res != float('inf') else -1

def leftmost_repeating_char_3(s):
    CHAR = 256  # Total possible ASCII characters
    visited = [False] * CHAR  # Initialize the count array
    
    res = -1
    # better right to left
    for i in range(len(s)-1,-1,-1):
        if visited[ord(s[i])]:
            res = i
        else:
            visited[ord(char)] = True
    return res 

def leftmost_non_repeating_char(s):
    CHAR = 256  # Total possible ASCII characters
    count = [0] * CHAR  # Initialize the count array
    
    # Fill the count array with occurrences of each character
    for char in s:
        count[ord(char)] += 1

    # Find the leftmost non-repeating character
    for char in s:
        if count[ord(char)] == 1:
            return char
    
    return None  # No non-repeating character found

# Example usage
s = "geeksforgeeks"
result = leftmost_non_repeating_char(s)
print("Leftmost Non-Repeating Character:", result)  # Output: f

def leftmost_non_repeating_char2(s):
    CHAR = 256  # Total possible ASCII characters
    freq_index = [-1] * CHAR  # Initialize the count array
   
    # storing index in array 
    for i in range(len(s)):
        if freq_index[ord(s[i])] == -1:
            freq_index[ord(char)] = i
        else:
             freq_index[ord(char)] = -2
    
    res = 1e9 
    for i in range(256):
        if freq_index[i]>0:
            res = min(res,freq_index[i])
            
    return res if res != float('inf') else -1 