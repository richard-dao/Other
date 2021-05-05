# Python
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        catWord1 = "";
        catWord2 = "";
        for x in range(0, len(word1)):
            catWord1 += word1[x]
        for x in range (0, len(word2)):
            catWord2 += word2[x]
        if (catWord1 == catWord2):
            return True
        else:
            return False
