#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    try:
        if idx >= 0:
            my_list[idx] = element
            return my_list
        else:
            return my_list
    except Exception as ex:
        return my_list
