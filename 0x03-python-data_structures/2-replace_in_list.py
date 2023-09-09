#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 and len(my_list) > idx:
        return my_list
    else:
        my_list[idx] = element
        return my_list
