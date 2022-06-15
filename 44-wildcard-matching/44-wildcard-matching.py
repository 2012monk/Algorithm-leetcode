class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        dp = {(n, m): 1}
        def f(i, j):
            if (i,j) in dp:
                return dp[i,j]
            if j == m:
                dp[i, j] = i == n
                return dp[i, j]
            if i >= n:
                dp[i, j] = p[j] == '*' and f(i, j + 1)
                return dp[i, j]
            dp[i, j] = 0
            if p[j] == '*':
                dp[i,j] = f(i, j + 1) or f(i + 1, j)
            if p[j] in (s[i], '?'):
                dp[i, j] = f(i + 1, j + 1)
            return dp[i, j]

        #f(0, 0)
        #print(dp)
        return f(0, 0)