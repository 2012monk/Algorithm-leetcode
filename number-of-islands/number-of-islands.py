class Solution:
    grid: list[list[str]]
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        mr, nr = range(m), range(n)

        land = 0
        def dfs(i, j):
            for nx, ny in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + nx, j + ny
                if x in mr and y in nr and grid[x][y] != '0':
                    grid[x][y] = '0'
                    dfs(x, y)
            return 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    land += dfs(i, j)
        return land
                    
        
        
        