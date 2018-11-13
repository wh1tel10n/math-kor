import sys
import os
# Go to the root directory of this project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from math_kor.basic import 더하기

class TestKorMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(더하기(1,2), 3)
