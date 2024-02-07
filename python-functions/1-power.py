#!/usr/bin/env python3
def pow(a, b):
    """
    Computes the value of a raised to the power of b.

    Args:
        a: base number
        b: exponent

    Returns:
        The value of a raised to the power of b.
    """
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
