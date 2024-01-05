#!/bin/env python3
# find peak in a list of unsorted integers

def find_peak(list_of_integers):
    for i in list_of_integers:
        if i == max(list_of_integers):
            return i
        else:
            continue