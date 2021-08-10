import unittest
class MyAtoiClass:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        lstS = list(s)
        resultString = ""
        while index < len(s):
            if lstS[index].isnumeric() is True or lstS[index] == "-":
                resultString = resultString + lstS[index]
            index = index + 1
        return int(resultString)

class MyAtoiClassTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(MyAtoiClass.myAtoi(self, "words and 987"), 987)