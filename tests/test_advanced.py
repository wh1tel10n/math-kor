import sys
import os
# Go to the root directory of this project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from math_kor.advanced import 최대공약수

class TestAdvancedMath(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(최대공약수(18,30), 6)
