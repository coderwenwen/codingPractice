class JewelsAndStones(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        https://leetcode.com/problems/jewels-and-stones/
        """
        index = 0
        count = 0
        while index < len(stones):
            if stones[index] in jewels:
                count = count + 1
            index = index + 1
        return count
