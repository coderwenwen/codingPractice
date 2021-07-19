import unittest

class PlusOneClass(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        https://leetcode.com/problems/plus-one/
        """
        if not digits:
            return digits
        elif len(digits) == 0:
            return digits
        else:
            if digits[len(digits)-1] != 9:
                digits[len(digits) - 1] = digits[len(digits)-1] + 1
            else:
                digits[len(digits) - 1] = 0
                digits[len(digits) - 2] = digits[len(digits)-2] + 1
        return digits

class PluOneTests(unittest.TestCase):
    def test_BaseCase(self):
        n = 1
        self.assertEqual(PlusOneClass.plusOne(self, n), 1)



