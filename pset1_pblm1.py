# -*- coding: utf-8 -*-
"""
Count vowels in a String

Created on Sat Jun 10 05:55:35 2017

@author: mtrem
"""

s = ''
counter = 0

for n in range(len(s)):
    if (s[n] == 'a' or s[n] == 'e' or s[n] == 'i' or s[n] == 'o' or s[n] == 'u'):
        counter += 1
    
print("Number of vowels: " + str(counter))    
        