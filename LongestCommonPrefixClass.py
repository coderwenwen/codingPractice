import unittest


class LongestCommonPrefixClass(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefixLetter = ""
        commonPrefixResult = ""
        maxLoop = len(min(strs))

        for indexCheck in range(0, maxLoop):
            for strIndex, str in enumerate(strs):
                if prefixLetter == "" or strIndex == 0:
                    prefixLetter = str[indexCheck]
                if prefixLetter != str[indexCheck] and strIndex != 0:
                    return commonPrefixResult
                if prefixLetter == str[indexCheck] and strIndex == (len(strs) - 1):
                    commonPrefixResult = commonPrefixResult + prefixLetter
                elif prefixLetter == str[indexCheck] and strIndex != (maxLoop - 1):
                    continue
        return commonPrefixResult



    


class LongestCommmonPrefixClassTest(unittest.TestCase):
    def test_none_array(self):
        strs = []
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "")

    def test_oneStrInArray(self):
        strs = ["one"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "one")

    def test_twoStrInArray(self):
        strs = ["one", "ong"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "on")

    def test_sameStrInArray(self):
        strs = ["one", "one"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "one")

    def test_twoStrNoPrefixInArray(self):
        strs = ["one", "ong", "onn"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "on")


    def test_diffStrLenthInArray(self):
        strs = ["one", "on"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "on")

    def test_diffStrLenthInArray2(self):
        strs = ["one", "on", "on", "on", "on"]
        self.assertEqual(LongestCommonPrefixClass.longestCommonPrefix(self, strs), "on")




