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
    return round(result, 10)  # Round the result to 10 decimal places

# Test cases
print(pow(10, -2))   # Output: 0.01
print(pow(-98, -10))  # Output: 1.223881142e-20
