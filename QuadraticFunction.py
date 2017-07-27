# -*- coding: utf-8 -*-
"""
 Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a⋅x2+b⋅x+c.

Created on Mon Jun 19 15:28:29 2017

@author: mtrem
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return (a * (x ** 2)) + (b * x) + c

print(evalQuadratic(2, 3, 4, 7))

    