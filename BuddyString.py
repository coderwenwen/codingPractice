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
        elif s == goal:
            setS = set(s)
            if len(setS) == len(s): #if they have the same lenth, it means each char is unique
                return False
            else:
                return True
        else:
            i = 0
            lstS = list(s)
            lstGoal = list(goal)
            isSwapped = False
            while i < len(lstS):
                if lstS[i] != lstGoal[i]:
                    isSwapped = True
                    temp = lstS[i]
                    lstS[i] = lstGoal[i]
                    lstGoal[i] = temp
                i = i + 1
            if ''.join(lstS) == ''.join(lstGoal) and isSwapped is True:
                return True
            elif len(set(s)) < len(s) and isSwapped is True:
                return True
        return False

class BuddyStringTest(unittest.TestCase):
    def test_EasyCase(self):
        self.assertEqual(BuddyString.buddyStrings(self, "abab", "abab"), True)

    def test_EasyCase2(self):
        self.assertEqual(BuddyString.buddyStrings(self, "ab", "ab"), False)

    def test_EasyCase3(self):
        self.assertEqual(BuddyString.buddyStrings(self, "aa", "aa"), True)

    def test_EasyCase4(self):
        self.assertEqual(BuddyString.buddyStrings(self, "ab", "ba"), True)

    def test_RepeatedLongWord(self):
        self.assertEqual(BuddyString.buddyStrings(self, "aaaaaaabc", "aaaaaaacb"), True)

    def test_RepeatedWord(self):
        self.assertEqual(BuddyString.buddyStrings(self, "abcd", "badc"), False)