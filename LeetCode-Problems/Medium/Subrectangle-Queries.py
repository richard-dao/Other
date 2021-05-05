# Python
class SubrectangleQueries(object):
    
    matrix = [] 

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.matrix = rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for x in range(row1, row2+1):
            for y in range (col1, col2+1):
                self.matrix[x][y] = newValue
        
        

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
