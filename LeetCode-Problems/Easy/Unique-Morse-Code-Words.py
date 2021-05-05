# Python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transforms = list()
        differents = list()
        count = 0
        for x in range(0, len(words)):
            convert = ""
            for y in range(0, len(words[x])):
                ascii = ord(words[x][y:y+1])
                ascii = ascii - 97
                convert += morse[ascii]
            transforms.append(convert)
        for x in range(0, len(transforms)):
            if (transforms[x] not in differents):
                count = count + 1
                differents.append(transforms[x])
            else:
                count = count
        return count
