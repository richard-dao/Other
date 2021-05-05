# Python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0;
        for x in range(0, len(stones)):
            for y in range(0, len(jewels)):
                if stones[x:x+1] == jewels[y:y+1]:
                    count += 1
        return count
        
