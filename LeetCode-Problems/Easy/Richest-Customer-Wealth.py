# Python
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        returnedInt = 0
        for x in range(0, len(accounts)):
            temp = 0
            for y in range(0, len(accounts[x])):
                temp += accounts[x][y]
            if (temp > returnedInt):
                returnedInt = temp
        return returnedInt
