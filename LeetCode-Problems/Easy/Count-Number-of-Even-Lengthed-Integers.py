# Python
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in range (0, len(nums)):
            numLength = len(str(nums[x]))
            if (numLength % 2 == 0):
                count = count + 1
        return count
