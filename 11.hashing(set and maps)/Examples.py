def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example
s = "swiss"
print(first_non_repeating(s))  # Output: 'w'

def longest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            current = num
            streak = 1
            while current + 1 in nums:
                current += 1
                streak += 1
            longest = max(longest, streak)
    
    return longest

# Example
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(arr))  # Output: 4

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
