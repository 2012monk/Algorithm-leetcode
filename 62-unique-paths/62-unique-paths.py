class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def f(m, n):
            if m == 1 or n == 1:
                return 1
            return f(m - 1, n) + f(m, n - 1)
        
        return f(m, n)