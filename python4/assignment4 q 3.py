#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 22:15:46 2023

@author: paraggupta
"""


import random
num_questions = 10
points = 0
for i in range(num_questions):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = int(input("What is {} x {}? ".format(num1, num2)))
    if answer == num1 * num2:
        points += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is {}.".format(num1 * num2))
print("You scored {} points.".format(points))