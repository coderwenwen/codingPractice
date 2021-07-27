import unittest
class ShuffleString(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        https://leetcode.com/problems/shuffle-string/
        """
        index = 0
        resultArray = [0] * len(indices)
        while index < len(indices):
            indice = indices[index]
            resultArray[indice] = s[index]
            index = index + 1
        return "".join(resultArray)
