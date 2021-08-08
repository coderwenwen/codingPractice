import math
import unittest
class ReverseString(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lstS = list(s)
        index = 0
        while index < math.floor(len(lstS)/2):
            temp = lstS[index]
            lstS[index] = lstS[len(s) - index - 1]
            lstS[len(s) - index - 1] = temp
            index = index + 1
        return ''.join(lstS)

class ReverseStringTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(ReverseString.reverseString(self, "hello"), "olleh")
