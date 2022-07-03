class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        box = [[0 for _ in range(3)] for _ in range(3)]
        row = [0] * 9
        col = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                c = 1<<int(board[i][j])
                if row[i]&c!=0 or col[j]&c!=0:
                    return False
                if box[i//3][j//3]&c:
                    return False
                box[i//3][j//3]|=c
                row[i]|=c
                col[j]|=c
        return True
                
        