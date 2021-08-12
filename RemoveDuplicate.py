import unittest
class RemoveDuplicate(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        prev = nums[0]
        while index < len(nums):
            if nums[index] > prev:
                prev = nums[index]
            else:
                nums.pop(nums[index])
            index = index + 1
        return len(nums)

class RemoveDuplicate(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(RemoveDuplicate.removeDuplicates(self, [1,2,2,3]), 3)