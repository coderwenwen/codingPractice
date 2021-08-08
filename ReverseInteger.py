import math
import unittest
class ReverseInteger(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strX = str(x)
        lstX = list(strX)
        index = 0
        lstResult = list()
        lstX.reverse()

        if lstX[len(lstX) - 1] == "-":
            lstResult.append("-")
            lstX.remove(lstX[len(lstX)- 1])

        isContinuedZero = True

        while index < len(lstX):
            if lstX[index] == 0 and isContinuedZero is True:
                isContinuedZero = True
            elif lstX[index] != 0 and isContinuedZero is True:
                isContinuedZero = False
                lstResult.append(lstX[index])
            else:
                lstResult.append(lstX[index])
            index = index + 1
        return int(''.join(lstResult))




class ReverseIntegerTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(ReverseInteger.reverse(self, 123), 321)

    def test_case2(self):
        self.assertEqual(ReverseInteger.reverse(self, 1534236469), 9646324351)
