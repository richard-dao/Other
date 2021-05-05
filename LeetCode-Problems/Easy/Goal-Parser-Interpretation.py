# Python
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        returnedString = "";
        
        for x in range(0, len(command)):
            if (command[x:x+1] == "G"):
                returnedString += "G"
            if (x < len(command)-1):
                if (command[x:x+2] == "()"):
                    returnedString += "o"
            if (x < len(command)-3):
                if (command[x:x+4] == "(al)"):
                    returnedString += "al"
        return returnedString
