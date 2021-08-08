import unittest
class FirstUniqueCharacter(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        keyValueDict = {}
        index = 0
        lstS = list(s)
        while index < len(lstS):
            if lstS[index] not in keyValueDict:
                keyValueDict[lstS[index]] = 1
            else:
                return index
            index = index + 1
        return -1

class FirstUniqueCharacterTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(FirstUniqueCharacter.firstUniqChar(self, "leetcode"), 2)