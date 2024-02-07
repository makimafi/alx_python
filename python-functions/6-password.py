def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    return True


if __name__ == "__main__":
    # Test cases
    print(validate_password("Password123"))  # True
    print(validate_password("abc123"))        # False
    print(validate_password("Password 123"))  # False
    print(validate_password("password123"))   # False
