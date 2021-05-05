# Python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rArr = list()
        for x in range(0, len(numbers)):
            for y in range(x+1, len(numbers)):
                if (numbers[x] + numbers[y] == target):
                    rArr.append(x+1)
                    rArr.append(y+1)
                    return rArr
        return rArr
        
