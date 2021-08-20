import unittest
class MoveZeroes(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
        """
        index = 0
        oriLength = len(nums)
        while index < oriLength:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                oriLength = oriLength - 1
            else:
                index = index + 1
        return nums

class MoveZeroesTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(MoveZeroes.moveZeroes(self, [1, 0, 0, 2, 0, 13, 0]), [1, 2, 13, 0, 0, 0])