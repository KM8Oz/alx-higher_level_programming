#!/usr/bin/python3
def pow(a, b):
    return "{:.0f}".format(a ** b) if b >= 0 else "{:.4g}".format(a ** b)
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
print(pow(10, -2))