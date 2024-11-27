num1 = 35
num1 = 35.0000000000000
num1 = 35.345678

# to set number upto 5 decimal places
print(f"{num1:.5f}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(17))  # Output: True
print(is_prime(18))  # Output: False


def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
print(hcf(12, 15))  # Output: 3
print(hcf(101, 103))  # Output: 1


def lcm(a, b):
    return (a * b) // hcf(a, b)

# Example
print(lcm(12, 15))  # Output: 60
print(lcm(101, 103))  # Output: 10403


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

# Example
print(prime_factors(56))  # Output: [2, 2, 2, 7]
print(prime_factors(97))  # Output: [97]


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

# Example
print(sieve_of_eratosthenes(50))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def are_coprime(a, b):
    return hcf(a, b) == 1

# Example
print(are_coprime(12, 15))  # Output: False
print(are_coprime(17, 19))  # Output: True


def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count

# Example
print(count_divisors(12))  # Output: 6 (1, 2, 3, 4, 6, 12)
print(count_divisors(17))  # Output: 2 (1, 17)


def sum_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

# Example
print(sum_divisors(12))  # Output: 28 (1 + 2 + 3 + 4 + 6 + 12)
print(sum_divisors(17))  # Output: 18 (1 + 17)


def is_perfect_number(n):
    return sum_divisors(n) - n == n

# Example
print(is_perfect_number(28))  # Output: True (1 + 2 + 4 + 7 + 14 = 28)
print(is_perfect_number(12))  # Output: False
