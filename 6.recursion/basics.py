def power(x, n):
    if n == 0:  # Base case
        return 1
    return x * power(x, n - 1)  # Recursive case

# Example
print(power(2, 3))  # Output: 8

def reverse_string(s):
    if len(s) == 0:  # Base case
        return s
    return s[-1] + reverse_string(s[:-1])  # Recursive case

# Example
print(reverse_string("hello"))  # Output: "olleh"


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)  # Recursive case
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)  # Recursive case

# Example
tower_of_hanoi(3, 'A', 'C', 'B')  


def print_subsets(s, idx=0, curr=[]):
    if idx == len(s):  # Base case
        print(curr)
        return
    print_subsets(s, idx + 1, curr)  # Recursive case without including s[idx]
    print_subsets(s, idx + 1, curr + [s[idx]])  # Recursive case including s[idx]

# Example
print_subsets([1, 2, 3])
