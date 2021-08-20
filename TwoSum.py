class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        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
        """
        index = 0
        diffMap = {}
        while index < len(nums):
            difference = target - nums[index]
            if difference not in diffMap.keys():
                diffMap[nums[index]] = index
            else:
                return [index, diffMap[difference]]
            index = index + 1
        return [0, 0]

