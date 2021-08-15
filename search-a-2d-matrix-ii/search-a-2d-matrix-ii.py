class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if t == matrix[row][col]:
                return True
            elif t < matrix[row][col]:
                col -= 1
            elif t > matrix[row][col]:
                row += 1
        return False
        
        
        