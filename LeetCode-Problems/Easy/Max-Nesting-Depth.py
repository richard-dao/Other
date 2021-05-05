# Python
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxCount = 0
        count = 0
        for x in range(0, len(s)):
            if s[x:x+1] == "(":
                count = count + 1
            if s[x:x+1] == ")":
                count = count - 1
            if count > maxCount:
                maxCount = count
        return maxCount
        
