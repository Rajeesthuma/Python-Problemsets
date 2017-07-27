# -*- coding: utf-8 -*-
"""
 program that guesses a secret number using Bisection search

Created on Sun Jun 18 11:09:02 2017

@author: mtrem
"""

print("Please think of a number between 0 and 100!")

# Initialise the values of low and high 

low = 0
high = 100
userInput = ''
guess = 0

while (True):
# Calculate guess
    guess = int (( low + high ) / 2 )

    print("Is your secret number " + str(guess) + "?")
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.")

    if (userInput == 'h'):
        #print(userInput)
        high = guess
    elif (userInput == 'l'):
        #print(userInput)
        low = guess
    elif (userInput == 'c'):
        #print(userInput) 
        break
        
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))   