#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a
    return round(result, 10)  # Round the result to 10 decimal places

# Test cases
print(pow(10, -2))
print(pow(-98, -10))

    result = 1

    # Handling negative exponents
    if b < 0:
        a = 1 / a
        b = -b

    # Exponentiation by squaring algorithm
    while b:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result

# Testing the function
if __name__ == "__main__":
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
