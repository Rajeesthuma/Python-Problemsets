# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:05:52 2017

@author: mtrem
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, e):
        # Returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).
        if e.getX() == self.getX() and e.getY() == self.getY():
            return True
        else:
            return False
    
    def __repr__(self):
        #  Returns a string that looks like a valid Python expression that could be used to recreate an object with the same value.
        return "Coordinate(" + str(self.getX()) + ", " + str(self.getY()) + ")"