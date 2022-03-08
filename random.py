# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:33:10 2022

@author: harsha
"""

from random import randint

def generateRandomNumber(start=0, end=100000):
    print('Random number -> ',randint(start,end))

# Generating random numbers without arguments    
generateRandomNumber()

# Generating random numbers with arguments    
generateRandomNumber(0,100)