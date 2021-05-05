# Python
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        returnedString = ""
        for x in range(0, len(indices)):
            for y in range(0, len(indices)):
                if (indices[y] == x):
                    returnedString += s[y:y+1]
        return returnedString
        
