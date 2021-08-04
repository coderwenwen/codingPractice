class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        https://leetcode.com/problems/buddy-strings/
        """
        i = 0
        while i + 1 < len(s):
            lst = list(s)
            lst[i], lst[i+1] = lst[i+1], lst[i]
            if ''.join(lst) == goal:
                return True
            i = i + 1
        return False

