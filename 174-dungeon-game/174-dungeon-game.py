class Solution:
    def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        
        n,m=len(mat),len(mat[0])
        @lru_cache(maxsize=None)
        def f(i,j):
            if i == n or j == m:
                return 10e9
            if i == n-1 and j == m - 1:
                return max(1-mat[i][j], 1)
            d,r = f(i + 1, j), f(i, j + 1)
            return max(1, min(d, r) - mat[i][j])
        return f(0,0)
            
                
                
                
            