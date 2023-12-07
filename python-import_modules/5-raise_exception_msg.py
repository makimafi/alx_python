#!/usr/bin/python3
def raise_exception_msg(message=""):
     raise nameerror(message)
# Test the function
if __name__ == " _main_ ":
    try:
        raise_exception_msg("c is fun")
    Except nameerror as ne:
        print(ne)