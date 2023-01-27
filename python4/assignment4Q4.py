#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:29:48 2023

@author: paraggupta
"""

for candies in range(200):
    if (candies%5!=2):
        continue
    if (candies%6!=3):
        continue
    if (candies%7!=2):
        continue
    print(str(candies),"is in the answer!")
    break