# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:07:25 2022

@author: rhegstrom

Write a python program to find the total number of ways to make change for $1

Examples: 100 pennies, or 75 pennies and 5 nickels .....

- fork the repository to YOUR Github account; work the problem, push the solution back up to your github account. turn in the URL
"""



for fifty in range(3):
#    print(f'fifty={fifty}')
    for quarter in range(5):
#        print(f'   quarter={quarter}')

        amt = fifty*50 + quarter*25
        if amt == 100:
            print(f'fifty={fifty} quarter={quarter}')

