class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = {}
        def f(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i > j:
                return 0
            dp[i,j] = f(i, j - 1)+1
            for k in range(i, j):
                if s[k] != s[j]:
                    continue
                dp[i, j] = min(dp[i, j], f(i, k) + f(k + 1, j - 1))
            return dp[i, j]
        return f(0, n - 1)