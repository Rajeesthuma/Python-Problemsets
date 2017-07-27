# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:15:40 2017

@author: mtrem
"""

import numpy


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    #index = len(L) - 1
    #element = 10
    #fn = 0
    
    #for item in L:
        #fn += item * (x ** index)
        #index -= 1
    
    #return(fn)
    p1 = numpy.poly1d(L)
    
#print(general_poly ([1, 2, 3, 4]))
    return p1

print(general_poly ([1, 2, 3, 4]))