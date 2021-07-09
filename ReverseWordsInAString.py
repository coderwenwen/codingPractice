import unittest


class ReverseWordsInAStringClass(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        https://leetcode.com/problems/reverse-words-in-a-string/
        """
        if s == "":
            return ""

        tempList = list(s)
        for frontIndex, letter in enumerate(tempList):
            backIndex = len(s)-frontIndex-1
            if backIndex > frontIndex:
                placeholder = tempList[backIndex]
                tempList[frontIndex] = placeholder
                tempList[backIndex] = letter
            else:
                break
        return "".join(str(x) for x in tempList)


class ReverseWordsInAStringIIITest(unittest.TestCase):
    def test_emptyStr(self):
        str = ""
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "")

    def test_OneWord(self):
        str = "abc"
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "cba")

    def test_TwoWord(self):
        str = "abc def"
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "fed cba")

    def test_Sentence(self):
        str = "Hi I am Wendy"
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "ydneW ma I iH")













