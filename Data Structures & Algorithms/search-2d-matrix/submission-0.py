class Solution:
    def matrixsearch(self, matrix, target, row_target, row, col):
        start = 0
        end = col-1
        while start <= end:
            mid = int(start+end)//2
            if matrix[row_target][mid] == target:
                return True
            elif matrix[row_target][mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

        return False



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][col-1] >=  target:
                if self.matrixsearch(matrix, target, i, row, col) == True:
                    return True
                    break

        return False
            