# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:26:51 2022

@author: harsha
"""

# a python program to convert kilometres to miles
def km():
    ki_me = float(input("Enter the no. of kms: "))
    print("{} kilometers equals {} miles".format(ki_me, ki_me*0.621))
    
    
km()


# a python program to convert celsius to fahrenheit
def cf():
    cel = float(input("Enter the temp in celsius: "))
    fah = (cel*(9/5))+32
    print('{}  celsius equals {} in fahrenheit'.format(cel, fah)  )
    
    
cf()6