#!usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
        return res
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {:.1f}".format(res))
