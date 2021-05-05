# Python
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        firstHalf = list()
        secondHalf = list()
        returnedList = list()
        for x in range(0, len(nums)/2):
            firstHalf.append(nums[x])
        for x in range(len(nums)/2, len(nums)):
            secondHalf.append(nums[x])
        
        i = 0;
        for x in range(0, len(nums)/2):
            returnedList.append(firstHalf[i])
            returnedList.append(secondHalf[i])
            i += 1
        return returnedList
