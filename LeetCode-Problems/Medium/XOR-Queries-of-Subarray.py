# Python
# Unfortunately this doesn't work as its Time Complexity is O(n^2), which ends up being TLE on Leetcode
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rArr = list()
        rSum = 0
        for x in range(0, len(queries)):
            start = queries[x][0]
            end = queries[x][1]
            rSum = arr[start]
            for y in range(start, end):
                rSum = (rSum ^ arr[y+1])
            rArr.append(rSum)
        return rArr
        
# Alternative with less Time Complexity
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rArr = list()
        leng = len(arr)
        xorTable = [0] * (leng+1)
        for x in range (0, leng):
            xorTable[x+1] = xorTable[x] ^ arr[x]
        for x in range (0, len(queries)):
            rArr.append(xorTable[queries[x][0]] ^ xorTable[(queries[x][1])+1])
        return rArr
            
