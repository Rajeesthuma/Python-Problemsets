# -*- coding: utf-8 -*-
"""
 program that prints the longest substring of s in which the letters occur in alphabetical order.

 For example, if s = 'azcbobobegghakl', then your program should print
 Longest substring in alphabetical order is: beggh
 
Created on Fri Jun 16 16:03:10 2017

@author: mtrem
"""

  
# String of letters in alphabetical order
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# input string
s = 'fwguvsabmbussybnqfd'

# Counter to keep track of characters in input string
counter = 0

# intialize the longest substring
longString = ''

# Keep track of previously found substring
prevString = ''


# Scan each letter in the Input string
# if the next letter is alphabetically higher order than last letter in substring then 
# append the string , else update the longString with current letter

# Compare newly found substring with the previous one
# In the case of ties, print the first substring, For example, if s = 'abcbcd', ans. abc 

# repeat until the end of the input string


while (counter < len(s)):
    if (longString == ''):
        longString = s[counter]
    else:  
        newString = longString[len(longString)-1]
        if (alphabet.find(newString) <= alphabet.find(s[counter])) :
            longString += s[counter]
        else:
            if (len(prevString) < len(longString)):
                prevString = longString
            longString = s[counter]
    counter += 1
    
if (len(prevString) == len(longString) or len(prevString) > len(longString)):
    print("Longest substring in alphabetical order is: " + prevString)   
else:
    print("Longest substring in alphabetical order is: " + longString)  
            
            
        
        
        
        
        
        
        
        
        