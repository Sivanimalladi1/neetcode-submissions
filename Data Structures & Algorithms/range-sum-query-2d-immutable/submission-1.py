class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                up = 0
                left = 0
                diag = 0
                if i > 0:
                    up = ans[i-1][j]
                   
                if j > 0 :
                    left = ans[i][j-1]
                   
                if i >0 and j >0:
                    diag = ans[i-1][j-1]

                ans[i][j] = up + left - diag +  self.matrix[i][j]
        
        

        result = 0
        up = ans[row1-1][col2] if row1 > 0 else 0
        left = ans[row2][col1-1] if col1 >0 else 0
        diag = ans[row1-1][col1-1] if row1 >0 and col1> 0 else 0
        result = ans[row2][col2]  - up - left + diag
        
        return result





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)