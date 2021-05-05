# Python
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0;
        for x in range(0, len(nums)):
            for y in range (x+1, len(nums)):
                if (nums[x] == nums[y]):
                    output += 1
        return output
