#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:54:13 2023

@author: paraggupta
"""

a=int(input("enter the year"))
if a%4==0 and a%100!=0:
    print("a is a leap year")
elif a%400==0:
    print("a is a leap year")
else:
    print("a is not a leap year")