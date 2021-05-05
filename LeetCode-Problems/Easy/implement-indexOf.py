# Python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (len(needle) < 1):
            return 0
        for x in range (0, len(haystack) - len(needle) + 1):
            if (haystack[x:x+(len(needle))] == needle):
                return x
        return -1
        
        
