# -*- coding: utf-8 -*-
"""
a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months.

Created on Wed Jun 21 19:26:33 2017

@author: mtrem
"""
#the outstanding balance on the credit card
balance = 3926

#annual interest rate as a decimal
annualinterestrate = 0.2

#monthly interest
monthinterest = annualinterestrate / 12

# intialise fixed monthly pay as 10$
fixedminmonthpay = 10

#update monthbalance intially to outstanding balance amount
monthbalance  = balance

month = 1

while (month <= 12):
    
    monthbalance = (monthbalance - fixedminmonthpay) + ((monthbalance - fixedminmonthpay) * monthinterest )
    
    month += 1
    
    if (monthbalance < 0):
        break
    if (monthbalance > 0 and month > 12):
        monthbalance = balance
        fixedminmonthpay += 10
        month = 1
    
print("Lowest Payment: " + str(fixedminmonthpay))    