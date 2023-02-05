class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        matrix_length=len(matrix)
        ith_length=len(matrix[0])
        self.prefix_sum=[[0 for i in range(ith_length)] for i in range(matrix_length)]
        self.prefix_sum=[[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(1,len(matrix[0])+1):
            self.prefix_sum[1][i]+=self.prefix_sum[1][i-1]+matrix[0][i-1]
        for j in range(2,len(matrix)+1):
            self.prefix_sum[j][1]+=self.prefix_sum[j-1][1]+matrix[j-1][0]
        for row in range(2,len(matrix)+1):
            for column in range(2,len(matrix[0])+1):
                self.prefix_sum[row][column]=self.prefix_sum[row-1][column]+self.prefix_sum[row][column-1]-self.prefix_sum[row-1][column-1]+matrix[row-1][column-1]
        
        for i in self.prefix_sum:
            print(i)

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # su=0
        # for i in range(row1,row2+1):
        #     su+=sum(self.matrix[i][col1:col2+1])
        print(self.prefix_sum[row2+1][col2+1],self.prefix_sum[row1][col2+1],self.prefix_sum[row2+1][col1],self.prefix_sum[row1][col1])
        
        su=self.prefix_sum[row2+1][col2+1]-self.prefix_sum[row1][col2+1]-self.prefix_sum[row2+1][col1]+self.prefix_sum[row1][col1]
        return su


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)