# Python
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum = 0
        
        if (len(arr) == 0 or arr == None):
            return 0
        for x in range(0, len(arr)):
            temp = 0
            for y in range (x, len(arr)):
                temp += arr[y]
                if ((y-x) % 2 == 0):
                    sum += temp
        return sum
