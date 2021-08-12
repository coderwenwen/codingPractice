class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet = set()
        index = 0
        while index < len(nums):
            if nums[index] not in numsSet:
                numsSet.add(nums[index])
            else:
                return True
            index = index + 1
        return False