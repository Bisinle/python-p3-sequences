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
        fibonacci_list.extend([0, 1])
        size = len(fibonacci_list)
        while size < 10:
            last_num = fibonacci_list[-1]
            snd_last_num = fibonacci_list[-2]
            fibonacci_list.append(last_num + snd_last_num)
            size += 1

        print(fibonacci_list)
