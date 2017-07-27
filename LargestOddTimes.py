# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:45:14 2017

@author: mtrem
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    dict = {}
    
    for item in L:
        if item not in dict.keys():
            temp1 = {item: 1}
            dict.update(temp1)
        else:
            val = dict.get(item)
            val += 1
            temp = {item: val}
            dict.update(temp)
            
    maxLst = []
    print(dict)
    
    for k, v in dict.items():
        if (v % 2 != 0):
            maxLst.append(k)
            
    if len(maxLst) > 0:
        return max(maxLst)
    else:
        return None
            
    
print(largest_odd_times([3,9,5,3,5,3]))      
            