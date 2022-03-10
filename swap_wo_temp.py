# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:03:20 2022

@author: harsha
"""

# a program to swap numbers without temp variable
a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))


def swap_num(n1, n2):
    n1 = n1 +n2
    n2 = n1- n2
    n1 = n1 - n2
    print("After swapping:", n1, n2)

swap_num(a, b)