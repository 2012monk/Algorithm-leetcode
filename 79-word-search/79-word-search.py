class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        d = [[0, 1],[0,-1],[1,0],[-1,0]]
        n,m=len(board),len(board[0])
        def f(i, j, x):
            if v[i][j]:
                return 0
            if board[i][j] == word[x] and x == len(word) - 1:
                return 1
            if board[i][j] != word[x]:
                return 0
            v[i][j] = 1
            for nx,ny in d:
                dx,dy = i + nx, j + ny
                if dx < 0 or dx >= n or dy < 0 or dy >= m:
                    continue
                if f(dx, dy, x + 1):
                    return 1
            v[i][j] = 0
            return 0
        v = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if f(i,j,0):
                    return 1
        return 0