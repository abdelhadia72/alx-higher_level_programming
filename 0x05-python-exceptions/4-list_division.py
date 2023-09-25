def list_division(my_list_1, my_list_2, list_length):

    own_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            own_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            own_list.append(0)
        except IndexError:
            print("out of range")
            own_list.append(0)
        else:
            own_list.append(result)

    return (own_list)
