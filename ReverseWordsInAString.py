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
        i = len(tempList) - 1
        j = -1
        stringResult = ""
        while i >= 0:
            item = tempList[i]
            if item == ' ':
                if j != -1:
                    wholeWord = ''.join(tempList[i+1:j+1])
                    if stringResult == "":
                        stringResult = wholeWord
                    else:
                        stringResult = stringResult + " " + wholeWord
                    j = -1

            else:
                # start of a whole word
                if j == -1:
                    j = i
                if i == 0 and tempList[i] != " " and stringResult == "":
                    stringResult = stringResult + ''.join(tempList[i:j+1])
                elif i == 0 and tempList[i] != " " and stringResult != "":
                    stringResult = stringResult + " " + ''.join(tempList[i:j+1])
            i = i - 1

        return stringResult


class ReverseWordsInAStringIIITest(unittest.TestCase):
    def test_emptyStr(self):
        str = ""
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "")

    def test_TwoWord(self):
        str = "  hello world  "
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "world hello")

    def test_ThreeWord(self):
        str = "a good   example"
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "example good a")

    def test_Sentence(self):
        str = "  Bob    Loves  Alice   "
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "Alice Loves Bob")

    def test_Sentence2(self):
        str = "the sky is blue"
        self.assertEqual(ReverseWordsInAStringClass.reverseWords(self, str), "blue is sky the")













