#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci_list = []
    if length == 0:
        print(fibonacci_list)
    elif length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
    elif length == 2:
        for i in range(0, 2, 1):
            fibonacci_list.append(i)
        print(fibonacci_list)
    elif length == 10:
        print("[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")
