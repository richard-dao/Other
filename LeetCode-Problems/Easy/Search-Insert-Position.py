# Python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for x in range(0, len(nums)):
            if (nums[x] == target):
                return x
        y = 0
        while (y < len(nums)):
            if (nums[y] < target):
                y = y + 1
            else:
                return y
        return y
