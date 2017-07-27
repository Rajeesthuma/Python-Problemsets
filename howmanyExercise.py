# -*- coding: utf-8 -*-
"""
write a procedure, called how_many, 
which returns the sum of the number of values associated with a dictionary

Created on Tue Jun 27 19:28:45 2017

@author: mtrem
"""


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    biggest = None
    
    for key,val in aDict.items():
        if (counter < len(val)):
            counter = len(val)
            biggest = key
            
    return biggest    

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))