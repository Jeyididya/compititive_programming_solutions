class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        len1 = len(matrix)
        len2 = len(matrix[0])
        self.pres = [[0 for j in range(len2+1)] for i in range(len1+1)]
        # print(self.pres)
        for i in range(len1):
            for j in range(len2):
                self.pres[i][j] = self.pres[i-1][j] + \
                    self.pres[i][j-1]-self.pres[i-1][j-1]+matrix[i][j]
        # for i in self.pres:
        #     print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.pres[row2][col2],self.pres[row2][col1-1] , self.pres[row1-1][col2] , self.pres[row1-1][col1])
        if row1 < 1 and col1 > 0:
            ans = self.pres[row2][col2]-self.pres[row2][col1-1]
        elif row1 < 1 and col1 < 1:
            ans = self.pres[row2][col2]
        elif row1 > 0 and col1 < 1:
            ans = self.pres[row2][col2]-self.pres[row1-1][col2]
        else:
            ans = self.pres[row2][col2]-self.pres[row2][col1-1] - \
                self.pres[row1-1][col2] + self.pres[row1-1][col1-1]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
