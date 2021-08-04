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
            while i < len(lstS):
                if lstS[i] != lstGoal[i]:
                    temp = lstS[i]
                    lstS[i] = lstGoal[i]
                    lstGoal[i] = temp
                i = i + 1

            if ''.join(lstS) == ''.join(goal):
                return True
        return False

class BuddyStringTest(unittest.TestCase):
    def test_EasyCase(self):
        self.assertEqual(BuddyString.buddyStrings(self, "abab", "abab"), True)
    def test_RepeatedWord(self):
        self.assertEqual(BuddyString.buddyStrings(self, "aaaaaaabc", "aaaaaaacb"), True)