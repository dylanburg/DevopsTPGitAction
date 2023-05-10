# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:03:41 2023

@author: dylan
"""
import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @staticmethod
    def soustraction(a, b):
        return a - b
    
class TestSimpleMath(unittest.TestCase):
    
    def test_addition_ok(self):
        self.assertEqual(SimpleMath.addition(1, 2), 3)
    
    def test_addition_nok(self):
        self.assertNotEqual(SimpleMath.addition(1, 3), 2)
        
    def test_soustraction_ok(self):
        self.assertEqual(SimpleMath.soustraction(2, 2), 0)
    
    def test_soustraction_nok(self):
        self.assertNotEqual(SimpleMath.soustraction(1, 3), 2)
    