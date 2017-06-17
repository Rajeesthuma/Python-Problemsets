# -*- coding: utf-8 -*-
"""
Program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl'


Created on Fri Jun 16 14:41:24 2017

@author: mtrem
"""

s = 'azcbobobegghakl'
count = 0

while 'bob' in s:
    count += 1 
    s = s[(s.find('bob') + 2):]

print("Number of times bob occurs is: " + str(count))