#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[:n]

if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))
