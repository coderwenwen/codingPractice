import unittest


class RomanToInteger(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/roman-to-integer/
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        romanToIntDict = {}
        romanToIntDict["I"] = 1
        romanToIntDict["V"] = 5
        romanToIntDict["X"] = 10
        romanToIntDict["L"] = 50
        romanToIntDict["C"] = 100
        romanToIntDict["D"] = 500
        romanToIntDict["M"] = 1000
        romanToIntDict["IV"] = 4
        romanToIntDict["IX"] = 9
        romanToIntDict["XL"] = 40
        romanToIntDict["XC"] = 90
        romanToIntDict["CD"] = 500
        romanToIntDict["CM"] = 900

        s.replace(" ", "")
        resultInt = 0
        if s == "":
            return 0
        else:
            for index, character in enumerate(s):
                if character in romanToIntDict:
                    if (character == "I" or character == "X" or character == "C") and (s[index+1] == "V"):
                        if ()
                        resultInt = resultInt + romanToIntDict[character]










class RomanToIntegerTestß(unittest.TestCase):
    def test_emptyStr(self):
        str = ""
        self.assertEqual(RomanToInteger.romanToInt(self, str), "")















