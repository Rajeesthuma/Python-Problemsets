# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 16:23:13 2017

@author: mtrem
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invDict = {}
    
    for value1 in d.values():
        invDict.setdefault(value1, None)
        
    for key2, value2 in invDict.items():
        pair = []
        for key1 in d.keys():
            if key2 == d.get(key1):
                pair.append(key1)
        invDict.update({key2:sorted(pair)})

        
    print(invDict)
    
    
dict_invert({1:10, 2:20, 3:30, 4:30})    