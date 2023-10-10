#!/usr/bin/python3
""" read/write from file """


def append_after(filename="", search_string="", new_string=""):
    """function append_after"""
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
