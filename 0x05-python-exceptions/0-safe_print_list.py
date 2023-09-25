#!/usr/bin/python3
def safe_print_list(my_list, x):
    i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            i += 1
        print("", end="\n")
        return (i)
    except IndexError:
        return (i)
