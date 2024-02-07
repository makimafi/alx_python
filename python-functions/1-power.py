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
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
