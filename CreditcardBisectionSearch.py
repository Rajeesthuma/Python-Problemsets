# -*- coding: utf-8 -*-
"""

program that uses these bounds and bisection search 
 to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.

Created on Thu Jun 22 05:36:09 2017

@author: mtrem
"""

#the outstanding balance on the credit card
balance = 999999

#annual interest rate as a decimal
annualInterestRate = 0.18

#monthly interest
monthinterest = annualInterestRate / 12

#Initialise the lower bound and upper bound of monthly payment
monthlyPaymentLower = balance / 12
monthlyPaymentUpper = ( balance * (( 1 + monthinterest) ** 12 ) ) / 12.0
fixedminmonthpay = ( monthlyPaymentLower + monthlyPaymentUpper  ) / 2

#update monthbalance intially to outstanding balance amount
monthbalance  = balance

month = 1

while (month <= 12):
    
    monthbalance = (monthbalance - fixedminmonthpay) + ((monthbalance - fixedminmonthpay) * monthinterest )
    
    month += 1
    
    if (monthbalance < 0 and monthbalance > -1):
        break
    if (monthbalance < 0 and monthbalance < -1 and month > 12):
        monthbalance = balance
        monthlyPaymentUpper = fixedminmonthpay 
        fixedminmonthpay = ( monthlyPaymentLower + monthlyPaymentUpper  ) / 2
        month = 1
        
    if (monthbalance > 0 and month > 12):
        monthbalance = balance
        monthlyPaymentLower = fixedminmonthpay 
        fixedminmonthpay = ( monthlyPaymentLower + monthlyPaymentUpper  ) / 2
        month = 1
        
    
print("Lowest Payment: %.2f " % fixedminmonthpay)  