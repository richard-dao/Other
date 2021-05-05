# Python
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        teamsLeft = n
        
        while (teamsLeft > 1):
            if (teamsLeft % 2 == 0):
                count += teamsLeft/2
                teamsLeft = teamsLeft/2
            if (teamsLeft % 2 == 1):
                count += teamsLeft/2
                teamsLeft = teamsLeft + 1
                teamsLeft = teamsLeft/2
        return count
        
