#!/usr/bin/python3
def common_elements(set_1, set_2):
    con = set(set_1) - (set(set_1) - set(set_2))
    return (con)
