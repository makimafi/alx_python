#!/usr/bin/env python3

def reverse_string(string):
    """
    Reverses a given string.

    Args:
    - string: The input string to be reversed.

    Returns:
    - reversed_string: The reversed string.
    """
    if not string:
        return string

    # Using slicing to reverse the string
    reversed_string = string[::-1]
    return reversed_string

if __name__ == "__main__":
    print(reverse_string("Hello"))
    print(reverse_string(""))
    print(reverse_string("madam"))
    print(reverse_string("Hello, World!"))
