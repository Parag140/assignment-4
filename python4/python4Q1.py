#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:47:07 2023

@author: paraggupta
"""

a=int(input("enter the marks"))
if a<=25:
    print("F")
if 25<a<=45:
    print("E")
if 45<a<=50:
    print("D")
if 50<a<=60:
    print("C")
if 60<a<=80:
    print("B")
else:
    print("A")