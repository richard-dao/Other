# Python
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        sum = start
        for x in range(1, n):
            sum = sum ^ (start + 2*x)
        return sum
