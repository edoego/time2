#!/usr/bin/env    python2.7

import unittest
import timecalc

class TestTime(unittest.TestCase):

    def test_chronos1(self):
        result = timecalc.chronos(2, [0, 3], [1, 5])
        expected = 4
        self.assertEqual(expected, result)
        
    def test_chronos2(self):
        result = timecalc.chronos(3, [-3, 3, 5], [0, 5, -1])
        expected = 12
        self.assertEqual(expected, result)
        
#logging test output to a file
if __name__ == '__main__':
    unittest.main()
