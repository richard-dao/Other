# Python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        palindrome = ""
        if (x < 0):
            return False
        if (x > 0 and x < 10):
            return True
        for x in range (len(y), -1, -1):
            palindrome += y[x:x+1]
        if (palindrome == y):
            return True
        return False
        
        
