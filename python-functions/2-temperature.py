def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = -b
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

# Test cases
print(pow(2, 2))     # Output: 4
print(pow(98, 2))    # Output: 9604
print(pow(98, 0))    # Output: 1
print(pow(100, -2))  # Output: 0.0001
print(pow(-4, 5))    # Output: -1024
print(pow(-98, -10)) # Output: very small positive number close to zero
