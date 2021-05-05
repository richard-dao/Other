# Python
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        arrList = list()
        
        for x in range(0, len(index)):
            arrList.insert(index[x], nums[x])
        return arrList
