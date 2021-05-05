# Python
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels =  ['a', 'e', 'i', 'o', 'u']
        a = lower(s[0:len(s)/2])
        b = lower(s[len(s)/2:len(s)])
        countA = 0
        countB = 0
        for x in range (0, len(s)):
            if (a[x:x+1] in vowels):
                countA = countA + 1
            if (b[x:x+1] in vowels):
                countB = countB + 1
        if (countA == countB):
            return True
        return False
            
        
