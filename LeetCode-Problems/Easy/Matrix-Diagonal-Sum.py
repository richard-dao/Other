# Python
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rSum = 0
        y = len(mat)-1
        for x in range (0, len(mat)):
            addLR = mat[x][x]
            addRL = mat[x][y]
            rSum = rSum + addLR + addRL
            y = y-1
        if (len(mat) % 2 == 1):
            rSum = rSum - mat[len(mat)/2][len(mat)/2]
        return rSum
        
            
            
