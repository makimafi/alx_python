import random

# This line should not change
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Adjust the sign of the last digit for negative numbers
if number < 0:
    last_digit = -last_digit

# Print the required output
print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
