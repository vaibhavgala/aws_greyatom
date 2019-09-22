# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:31:25 2019

@author: Winchester
"""

import unittest
import numpy

def multiply(x,y):
    try:
        z = 5
        return x*y
    except TypeError as e:
        return 'Type Error'#: You have passed two strings which cannot be multiplied'
        
class TestUM(unittest.TestCase):

    def __init__(self):
        self.x = 2
        pass

    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)

    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
        
    def test_strings_a_b(self):
        self.assertEqual(multiply(3,numpy.nan),'Type Error')
        
test_obj = TestUM()

if __name__ == '__main__':
    unittest.main()