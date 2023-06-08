#!/usr/bin/python3
def pow(a, b):
    return "{:.0f}".format(a ** b) if b >= 0 else "{:.4f}".format(a ** b).rstrip('0')
