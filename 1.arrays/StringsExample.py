def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Example
s = "hello"
print(reverse_string(s))  # Output: "olleh"


def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

# Example
s = "radar"
print(is_palindrome(s))  # Output: True


def first_non_repeating_char(s):
    for i in range(len(s)):
        found_duplicate = False
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                found_duplicate = True
                break
        if not found_duplicate:
            return s[i]
    return -1

# Example
s = "swiss"
print(first_non_repeating_char(s))  # Output: "w"


def count_substring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count

# Example
s = "hellohello"
sub = "hello"
print(count_substring(s, sub))  # Output: 2


def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

# Example
s = "geeksforgeeks"
print(remove_duplicates(s))  # Output: "geksfor"


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1, freq2 = {}, {}
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
    return freq1 == freq2

# Example
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # Output: True


def permute(s, i=0):
    if i == len(s)-1:
        print(s, end=" ")
        return
    for j in range(i,len(s)):
        s[i],s[j] = s[j],s[i]
        permute(s,i+1)
        s[i],s[j] = s[j],s[i]


def permutations(s, current=""):
    if len(s) == 0:
        print(current, end=" ")
        return
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        permutations(new_s, current + s[i])

# Example
s = "abc"
permutations(s)  # Output: "abc acb bac bca cab cba"



def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for i in range(1, len(strings)):
        temp = ""
        for j in range(min(len(prefix), len(strings[i]))):
            if prefix[j] == strings[i][j]:
                temp += prefix[j]
            else:
                break
        prefix = temp
        if not prefix:
            break
    return prefix

# Example
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    combined = s1 + s1
    for i in range(len(combined) - len(s2) + 1):
        if combined[i:i + len(s2)] == s2:
            return True
    return False

# Example
s1 = "abcde"
s2 = "cdeab"
print(is_rotation(s1, s2))  # Output: True


def longest_palindromic_substring(s):
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    max_length = 0
    result = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if is_palindrome(substr) and len(substr) > max_length:
                max_length = len(substr)
                result = substr
    return result

# Example
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

# if 2 string s and t are equal then in new_str = s + t
#  new_str  every character is divisible by 2