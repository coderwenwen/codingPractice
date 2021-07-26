import unittest
class MaximumSubArray(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode.com/problems/maximum-subarray/
        """
        index = 0
        totalCount = 0
        totalCountAlt = 0
        shouldCompare = False
        while index < len(nums):
            if nums[index] > 0 and shouldCompare is False:
                totalCount = totalCount + nums[index]
            elif nums[index] > 0 and shouldCompare is True:
                totalCountAlt = totalCountAlt + nums[index]
                if totalCountAlt > totalCount:
                    totalCount = totalCountAlt
                    totalCountAlt = 0
            elif nums[index] <= 0:
                shouldCompare = True
            index = index + 1
        return totalCount

    class RomanToIntegerTest(unittest.TestCase):
        def test_emptyRomanChar(self):
            str = [1]
            self.assertEqual(MaximumSubArray.maxSubArray(self, str), 1)

        def test_2ItemInArray(self):
            str = [1, -3]
            self.assertEqual(MaximumSubArray.maxSubArray(self, str), 1)

        def test_2SubArrays(self):
            str = [-1, 3, 5, -10, 5, 5]
            self.assertEqual(MaximumSubArray.maxSubArray(self, str), 10)

        def test_2SubArrays(self):
            str = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
            self.assertEqual(MaximumSubArray.maxSubArray(self, str), 6)



