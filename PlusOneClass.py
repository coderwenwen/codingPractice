import unittest

class PlusOneClass(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        https://leetcode.com/problems/plus-one/
        """
        if len(digits) == 0:
            return digits
        else:
            index = len(digits)-1
            shouldIncrement = False
            while index >= 0:
                if digits[index] != 9:
                    if index == len(digits) - 1 or shouldIncrement:
                        digits[index] = digits[index] + 1
                        shouldIncrement = False
                    index = index - 1
                elif digits[index] == 9:
                    if shouldIncrement:
                        digits[index] = 0
                    elif index == len(digits) - 1:
                        digits[index] = 0
                        shouldIncrement = True
                    index = index - 1
            if shouldIncrement:
                digits.insert(0, 1)
        return digits

class PluOneTests(unittest.TestCase):
    def test_BaseCase(self):
        n = [1]
        self.assertEqual(PlusOneClass.plusOne(self, n), [2])

    def test_TwoDigitsCase(self):
        n = [1, 2]
        self.assertEqual(PlusOneClass.plusOne(self, n), [1, 3])

    def test_TwoDigitsWithNineCase(self):
        n = [1, 9]
        self.assertEqual(PlusOneClass.plusOne(self, n), [2, 0])

    def test_NintyNineCase(self):
        n = [9, 9]
        self.assertEqual(PlusOneClass.plusOne(self, n), [1, 0, 0])



