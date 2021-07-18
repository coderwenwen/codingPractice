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
        romanToIntDict["IV"] = 4
        romanToIntDict["IX"] = 9
        romanToIntDict["X"] = 10
        romanToIntDict["XL"] = 40
        romanToIntDict["XC"] = 90
        romanToIntDict["C"] = 100
        romanToIntDict["CD"] = 500
        romanToIntDict["CM"] = 900

        romanToIntDict["V"] = 5
        romanToIntDict["L"] = 50
        romanToIntDict["D"] = 500
        romanToIntDict["M"] = 1000

        s.replace(" ", "")
        resultInt = 0
        if s == "":
            return 0
        else:
            index = 0
            while index < len(s):
                character = s[index]
                if character == "V" or character == "L" or character == "D" or character == "M":
                    if character in romanToIntDict:
                        resultInt = resultInt + romanToIntDict[character]
                        index = index + 1
                else:
                    if index + 1 < len(s):
                        if s[index] + s[index+1] in romanToIntDict:
                            resultInt = resultInt + romanToIntDict[s[index] + s[index+1]]
                            index = index + 2
                        else:
                            resultInt = resultInt + romanToIntDict[s[index]]
                            index = index + 1
                    else:
                        resultInt = resultInt + romanToIntDict[s[index]]
                        index = index + 1
            return resultInt



class RomanToIntegerTest(unittest.TestCase):
    def test_emptyRomanChar(self):
        str = ""
        self.assertEqual(RomanToInteger.romanToInt(self, str), 0)

    def test_OneRomanChar(self):
        str = "V"
        self.assertEqual(RomanToInteger.romanToInt(self, str), 5)

    def test_OneRomanChar(self):
        str = "L"
        self.assertEqual(RomanToInteger.romanToInt(self, str), 50)

    def test_TwoRomanChar(self):
        str = "XL"
        self.assertEqual(RomanToInteger.romanToInt(self, str), 40)

    def test_ThreeRomanChar(self):
        str = "III"
        self.assertEqual(RomanToInteger.romanToInt(self, str), 3)

    def test_ComplexRomanChar(self):
        str = "MCDXXVI"
        self.assertEqual(RomanToInteger.romanToInt(self, str), 1476)















