#!/usr/bin/python3
""" find peak in a list """


def find_peak(new_list):
    lst = new_list
    if lst == []:
        return None
    length = len(lst)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]
        if lst[mid - 1] > lst[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return lst[start]
