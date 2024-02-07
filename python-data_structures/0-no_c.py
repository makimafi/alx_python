#!/usr/bin/python3
def no_c(my_string):
    """Removes all occurrences of 'c' and 'C' from the given string."""
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
