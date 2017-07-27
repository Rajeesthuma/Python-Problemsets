# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:35:19 2017

@author: mtrem
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    newStr = ""
    
    for letter in s:
        if letter not in vowels:
            newStr += letter
            
    print(newStr)
            
            
     