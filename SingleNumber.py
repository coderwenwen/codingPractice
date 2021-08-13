class SingleNumber(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
        """
        index = 0
        resultFromNums = 0
        while index < len(nums):
            resultFromNums ^= nums[index]
            index = index + 1
        return resultFromNums