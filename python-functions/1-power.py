def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = -b

    result = 1
    for _ in range(b):
        result *= a
    return result

# Test cases
print(pow(2, 2))    # Expected output: 4
print(pow(-2, 2))    # Expected output: 4
print(pow(10, -2))   # Expected output: 0.01
print(pow(-98, -10)) # Expected output: 1.223881142011411e-20
