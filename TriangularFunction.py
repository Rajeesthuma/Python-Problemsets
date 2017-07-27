# -*- coding: utf-8 -*-
"""
Write a function is_triangular that meets the specification below.

A triangular number is a number obtained by the continued summation of integers starting from 1. 
 
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
Created on Sat Jul  1 14:26:14 2017

@author: mtrem
"""
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    start = 0
    sum = 0
    
    while (sum <= k):
        start += 1
        sum += start
        if (sum == k):
            return True
        
    return False        

print(is_triangular(-2))
        
        
