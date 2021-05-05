# Python
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        decodedArray = list()
        decodedArray.append(first)
        temp = 0;
        for x in range (0, len(encoded)):
            temp = encoded[x] ^ decodedArray[x]
            decodedArray.append(abs(temp))
        return decodedArray
