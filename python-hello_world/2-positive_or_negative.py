# 2-positive_or_negative.py

# Importing required module
import random

# Assigning a random signed number to the variable number
number = random.randint(-10, 10)

# Checking if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
