#!/usr/bin/python3
""" Create a pascal triangle """


def pascal_triangle(n):
    """ Function to create triangle"""
    if (n <= 0):
        return []

    for line in range(1, n+1):
        num = 1
        for i in range(1, line+1):
            print(num, end=" ")
            num = int(num * (line - i) / i)
        print("")
