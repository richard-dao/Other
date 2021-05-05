# Python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        if (len(s) == 0):
            return 0
        for x in range (len(s)-1, -1, -1):
            if (s[x:x+1] == " " and count > 0):
                return count
            if (s[x:x+1] != " "):
                count = count + 1
        return count
        
