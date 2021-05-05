# Python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        booleanList = list()
        max = 0;
        for x in candies:
            if x > max:
                max = x  
        for x in candies:
            if x + extraCandies >= max:
                booleanList.append(True)
            else:
                booleanList.append(False)
        return booleanList
