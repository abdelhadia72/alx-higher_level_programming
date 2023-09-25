#!/usr/bin/python3
def safe_print_list(my_list, x):
    c = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            c += 1
        except IndexError:
            pass
    print()
    return (c)
