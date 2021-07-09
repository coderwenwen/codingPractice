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

        tempList = list(s)
        tempWord = ""
        result = ""
        for letter in enumerate(tempList):
            if letter != "":
                tempWord += letter
            else:
                result += ReverseWordsInAStringIIIClass.reverseWord(self, tempWord) + " "
                tempWord = ""
        return result

    def reverseWord(self, s):
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
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "")

    def test_OneWord(self):
        str = "Let's take LeetCode contest"
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "s'teL ekat edoCteeL tsetnoc")

    def test_TwoWord(self):
        str = "God Ding"
        self.assertEqual(ReverseWordsInAStringIIIClass.reverseWords(self, str), "doG gniD")













