# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:07:25 2022

@author: Roger Hegstrom (rhegstrom@avc.edu)

Write a python program to find the total number of ways to make change for $1

Examples: 100 pennies, or 75 pennies and 5 nickels .....

- fork the repository to YOUR Github account; work the problem, push the solution back up to your github account. turn in the URL
"""


combos = 0
comboList = []

print("""
Calculating total combinations to make change for 1 dollar...
-------------------------------------------------------------
""")


for fifty in range(3):
    for quarter in range(5):
        for dime in range(11):
            for nickle in range(21):
                for penny in range(101):
                    amt = (fifty * 50
                          + quarter * 25
                          + dime * 10
                          + nickle * 5
                          + penny)
                    
                    if amt == 100:
                        combos += 1
                        comboList.append({'Half-Dollar': fifty, 
                                          'Quarter': quarter, 
                                          'Dime': dime, 
                                          'Nickle': nickle, 
                                          'Penny': penny})
                        



for e in comboList:
    l = [str(it[1])+' '+it[0]+('s' if it[1] != 1 else "") for it in e.items() if it[1] > 0]
    print(', '.join(l))
    
print(f'\n\nThere are {combos} total ways to make change for a $1...')                          
