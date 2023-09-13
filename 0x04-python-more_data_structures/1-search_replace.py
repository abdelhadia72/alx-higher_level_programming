#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    cp_list = my_list[:]
    while i < len(cp_list):
        if cp_list[i] == search:
            cp_list[i] = replace
        i += 1
    return cp_list
