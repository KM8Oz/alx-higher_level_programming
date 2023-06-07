#!/usr/bin/python3
for num in range(8):
    for n in range(num, 9):
        if n != 9 and num != 8:
            print("{:d}{:d},".format(num, n), end=' ')
        else:
            print("{:d}{:d},".format(num, n))
