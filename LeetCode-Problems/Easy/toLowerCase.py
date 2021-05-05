# Python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        selected = 0
        rString = ""
        for x in range(0, len(str)):
            selected = ord(str[x:x+1])
            if (selected < 91 and selected >= 65):
                rString += chr(selected + 32)
            else:
                rString += chr(selected)
        return rString
