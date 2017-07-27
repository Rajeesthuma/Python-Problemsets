# -*- coding: utf-8 -*-
"""

program to calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month

Created on Wed Jun 21 19:00:23 2017

@author: mtrem
"""

#the outstanding balance on the credit card
balance = 484

#annual interest rate as a decimal
annualInterestRate = 0.2

#minimum monthly payment rate as a decimal      
monthlyPaymentRate = 0.04

#month counter
month = 0

while (month < 12):

    #Monthly interest rate= (Annual interest rate) / 12.0
    monthlyInterestRate = annualInterestRate / 12.0

    #Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    minimumMonthlyPayment = monthlyPaymentRate * balance

    #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    monthlyUnpaidBalance = balance - minimumMonthlyPayment

    #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    #update balance
    balance = updatedBalanceEachMonth
    
    month += 1
    
print("Remaining balance: %.2f" % balance)    