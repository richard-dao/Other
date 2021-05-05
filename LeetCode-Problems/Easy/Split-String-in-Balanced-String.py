# Python
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        balStr = 0
        for x in range(0, len(s)):
            if s[x:x+1] == "L":
                balStr = balStr + 1
            else:
                balStr = balStr - 1
            if balStr == 0:
                count = count + 1
        return count
