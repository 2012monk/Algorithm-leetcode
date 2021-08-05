class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        land = 0
        def dfs(i, j):
            dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
            for nx, ny in zip(dx, dy):
                x, y = i + nx, j + ny
                if x in range(m) and y in range(n) and not v[x][y] and grid[x][y] != '0':
                    v[x][y] = ~v[x][y]
                    dfs(x, y)
            return 1
        
        for i in range(m):
            for j in range(n):
                if not v[i][j] and grid[i][j] == '1':
                    land += dfs(i, j)
        return land
                    
        
        
        