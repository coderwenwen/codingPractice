import unittest

class PlusOneClass(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        https://leetcode.com/problems/plus-one/
        """
        if not digits or len(digits) == 0:
            return digits
        else:
            index = len(digits)-1
            shouldIncrement = False
            while index >= 0:
                if digits[index] != 9:
                    digits[index] = digits[index] + 1
                    if shouldIncrement:
                        digits[index] = digits[index] + 1
                else:
                    digits[index] = 0
                    shouldIncrement = True
                    if shouldIncrement and index == 0:
                        digits.insert(0, 1)
        return digits

class PluOneTests(unittest.TestCase):
    def test_BaseCase(self):
        n = 1
        self.assertEqual(PlusOneClass.plusOne(self, n), 1)



