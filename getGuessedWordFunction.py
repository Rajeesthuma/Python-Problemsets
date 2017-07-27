# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:26:08 2017

@author: mtrem
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = "";
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord += " _ "
        else:
            guessedWord += letter
            
    return guessedWord       

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))