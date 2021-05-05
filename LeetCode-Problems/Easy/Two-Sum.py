# Python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        outputList = list()
        for x in range (0, len(nums)):
            for y in range (0, len(nums)):
                if (x != y):
                    if (nums[x] + nums[y] == target):
                        outputList.append(x)
                        outputList.append(y)
                        return outputList;
        return outputList;
        
