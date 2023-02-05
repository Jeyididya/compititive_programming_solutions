class NumMatrix:

    def __init__(self, matrix):
        self.matrix=[i for i in matrix]
    def sumRegion(self, row1, col1, row2, col2):
      for i in self.matrix:
        print(i)
      print(self.matrix[2][1],self.matrix[4][3])


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
# [2,1,4,3],[1,1,2,2],[1,2,2,4]
param_1 = obj.sumRegion(2,1,4,3)