import unittest
class BuddyString(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        https://leetcode.com/problems/buddy-strings/
        """
        if len(s) != len(goal):
            return False
        else:
            i = 0
            lstS = list(s)
            lstGoal = list(goal)
            isSwapped = False
            hasSameCharacter = False
            while i < len(lstS):
                if lstS[i] != lstGoal[i]:
                    isSwapped = True
                    temp = lstS[i]
                    lstS[i] = lstGoal[i]
                    lstGoal[i] = temp
                i = i + 1

            if ''.join(lstS) == ''.join(goal) and isSwapped is True:
                return True
        return False

class BuddyStringTest(unittest.TestCase):
    def test_EasyCase(self):
        self.assertEqual(BuddyString.buddyStrings(self, "abab", "abab"), True)

    def test_EasyCase2(self):
        self.assertEqual(BuddyString.buddyStrings(self, "ab", "ab"), False)

    def test_EasyCase3(self):
        self.assertEqual(BuddyString.buddyStrings(self, "aa", "aa"), True)

    def test_RepeatedWord(self):
        self.assertEqual(BuddyString.buddyStrings(self, "aaaaaaabc", "aaaaaaacb"), True)