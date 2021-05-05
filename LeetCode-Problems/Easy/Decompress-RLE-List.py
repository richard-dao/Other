# Python
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returnedList = list()
        pair = [0, 1]
        x = 0
        while (x < len(nums)):
            pair[0] = nums[x]
            pair[1] = nums[x+1]
            x = x+2
            for y in range (0, pair[0]):
                returnedList.append(pair[1])
        return returnedList
