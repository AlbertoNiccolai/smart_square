"""@author AN
"""

import unittest

from smart_square.core import square

class TestCore(unittest.TestCase):

    def test_float(self):
        """ Method which tests the correctness of the square function"""
        self.assertAlmostEqual(square(2.), 4.)

if __name__ == '__main__':
    unittest.main()
