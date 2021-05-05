# Python
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        returnedStr = "";
        for x in range(0, len(address)):
            if address[x] == ".":
                returnedStr += ("[.]")
            else:
                returnedStr += (address[x])
        return returnedStr
