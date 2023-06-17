#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return [{**a_dictionary, key: a_dictionary.get(key)*2} for key in a_dictionary][-1]
