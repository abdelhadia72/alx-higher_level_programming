#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        self.sort()
        print(self)
