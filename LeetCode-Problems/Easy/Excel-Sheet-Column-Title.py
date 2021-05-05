# Python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        number = ''
        x = n
        rStr = ""
        while (x > 0):
            number = chr(((x-1) % 26)+ 65)
            rStr += number
            x = (x-1) / 26
        return rStr[::-1]
