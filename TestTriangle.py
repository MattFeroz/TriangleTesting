# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    #Invalid Inputs of Large Numbers, Negative Numbers, and letters instead of numbers
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(100,150,201),'InvalidInput','Invalid')
        
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-3,-4,-5),'InvalidInput','Invalid')
        
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle('two', 3, 10),'InvalidInput','Invalid')

     #Examples of inputs that are not triangles
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','Invalid')
        
    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(5,11,4),'NotATriangle','Invalid')
    
    #Examples of inputs that are right Triangles
  
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
  
    #Examples of inputs that are Scalene Triangles

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(3,5,7),'Scalene','3,5,7 is a Scalene triangle')
        
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(4,11,8),'Scalene','4,11,8 is a Scalene triangle')

    #Examples of inputs that are Equilateral Triangles


    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 is a Equilateral triangle')
    
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is a Equilateral triangle')

    #Examples of inputs that are Isosceles Triangles


    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is a Isosceles triangle')
                    
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,7),'Isosceles','5,5,7 is a Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

