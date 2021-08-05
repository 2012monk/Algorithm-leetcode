class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        land = 0
        def dfs(i, j):
            dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
            for p in range(4):
                x, y = i + dx[p], j + dy[p]
                if 0<= x< m and 0 <= y < n and grid[x][y] != '0':
                    grid[x][y] = '0'
                    dfs(x, y)
            return 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    land += dfs(i, j)
        return land
                    
        
        
        