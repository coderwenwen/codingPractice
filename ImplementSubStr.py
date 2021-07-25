import unittest

class ImplementSubStr(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        https://leetcode.com/problems/implement-strstr/
        """
        if len(needle) == 0:
            return 0
        else:
            LeftPtr = 0
            RightPtr = len(needle) - 1
            while RightPtr < len(haystack):
                if haystack[LeftPtr:(RightPtr+1):1] == needle:
                    return LeftPtr
                LeftPtr = LeftPtr + 1
                RightPtr = RightPtr + 1
            return -1

class ImplementSubStrTests(unittest.TestCase):
    def test_BaseCase(self):
        self.assertEqual(ImplementSubStr.strStr(self, "", ""), 0)

    def test_EmptyHayStackCase(self):
        self.assertEqual(ImplementSubStr.strStr(self, "", "a"), -1)

    def test_HelloCase(self):
        self.assertEqual(ImplementSubStr.strStr(self, "Hello", "ll"), 2)
