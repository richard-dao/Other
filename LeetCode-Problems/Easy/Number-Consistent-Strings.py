# Python
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0;
        allowedSet = set()
        for x in range(0, len(allowed)):
            allowedSet.add(allowed[x:x+1])
        for x in range (0, len(words)):
            isConsistent = True
            for y in range (0, len(words[x])):
                if (words[x][y:y+1] not in allowedSet):
                    isConsistent = False
                    break
                isConsistent = True
            if (isConsistent):
                count = count + 1
        return count
