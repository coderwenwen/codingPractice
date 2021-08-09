import unittest
class ValidPalindrome(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charStr = ''.join(x for x in s if x.isdigit() or x.isalpha()).lower()
        charStrCopy = charStr
        if charStrCopy[::-1] == charStr:
            return True
        else:
            return False

class ValidPalindromeTest(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(ValidPalindrome.isPalindrome(self, "A man, a plan, a canal: Panama"))

    def test_case2(self):
        self.assertFalse(ValidPalindrome.isPalindrome(self, "0P"))