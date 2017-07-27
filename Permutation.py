# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:15:18 2017

@author: mtrem
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    dict1 = {}
    dict2 = {}
    
    if (len(L1) == 0 and len(L2) == 0):
        return (None, None, None)
    
    elif (len(L1) == len(L2)):    
    
        for item in L1:
            if item not in dict1.keys():
                temp1 = {item: 1}
                dict1.update(temp1)
            else:
                val = dict1.get(item)
                val += 1
                temp = {item: val}
                dict1.update(temp)
        #print(dict1)
        
        for item in L2:
            if item not in dict2.keys():
                temp1 = {item: 1}
                dict2.update(temp1)
            else:
                val = dict2.get(item)
                val += 1
                temp = {item: val}
                dict2.update(temp)    
            
        maxValue = None
        maxElement = None
    
        if (dict1 == dict2):   
            maxValue = max(dict2.values())
            for key in dict2.keys():
                if (dict2.get(key) == maxValue):
                    maxElement = key
                
            return (maxElement, maxValue, type(maxElement))
        else:
            return False  
    
    
    else:
        return False

L1 = [1, 2, 1]
L2 = [2, 1, 2]
print(is_list_permutation(L1, L2))
        
    
    
