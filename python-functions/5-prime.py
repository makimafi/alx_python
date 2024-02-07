def is_prime(number):
    # Check if number is less than 2, in which case it cannot be prime
    if number < 2:
        return False

    # Check if number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Test cases
if __name__ == "__main__":
    print(is_prime(17))  # True
    print(is_prime(15))  # False
    print(is_prime(-5))  # False
    print(is_prime(0))   # False
