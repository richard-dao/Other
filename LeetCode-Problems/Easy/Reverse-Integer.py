# Python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x;
        if (x < 0):
            x = -x
        num = str(x)[::-1]
        num = int(num)
        if (num < -(2**31) or num > 2**31 - 1):
            return 0
        if (neg < 0):
            return -num;
        return num;
