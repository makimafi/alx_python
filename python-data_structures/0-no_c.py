def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

# Test cases
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))