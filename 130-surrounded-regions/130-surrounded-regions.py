class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n,m = len(board), len(board[0])
        v = [[0] * m for _ in range(n)]
        def f(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if v[i][j] or board[i][j] == 'X':
                return 1
            v[i][j] = 1

            ret = 1
            for dx,dy in d:
                x = i + dx
                y = j + dy
                ret = ret & f(x, y)
            return ret
        def g(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 
            if board[i][j] == 'X':
                return 
            board[i][j] = 'X'

            for dx,dy in d:
                x = i + dx
                y = j + dy
                g(x,y)
        for i in range(n):
            for j in range(m):
                if v[i][j] or board[i][j] == 'X':
                    continue
                if f(i,j):
                    g(i,j)
        
                
