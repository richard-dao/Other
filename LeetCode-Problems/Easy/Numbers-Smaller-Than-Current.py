# Python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returnedList = list()
        count = 0
        for x in range (0, len(nums)):
            for y in range (0, len(nums)):
                if (nums[x] > nums[y]):
                    count = count + 1
            returnedList.append(count)
            count = 0
        return returnedList
