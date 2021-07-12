import unittest


class ReverseWordsInAStringIIIClass(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        https://leetcode.com/problems/reverse-words-in-a-string-iii/
        """
        if s == "":
            return ""

        tempList = s.split()
        wordCount = len(tempList)
        if wordCount == 0:
            return ""

        else:
            index = 0
            stringResult = ""
            while index < wordCount:
                word = tempList[index]
                reverseWord = word[::-1]
                if stringResult == "":
                    stringResult = reverseWord
                else:
                    stringResult = stringResult +  " " + reverseWord
                index = index + 1
            return stringResult

class ReverseWordsInAStringIIITest(unittest.TestCase):
    def test_emptyStr(self):
        str = ""
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "")


    def test_OneWord(self):
        str = "Let's take LeetCode contest"
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "s'teL ekat edoCteeL tsetnoc")

    def test_TwoWord(self):
        str = "God Ding"
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "doG gniD")













