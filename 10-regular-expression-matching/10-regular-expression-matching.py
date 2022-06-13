class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return 0
        n,m = len(s),len(p)
        dp = [[0]*(m+1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(m):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = 1
        
        for i in range(n):
            for j in range(m):
                if p[j] == '.' or s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    if p[j - 1] == '.' or s[i] == p[j - 1]:
                        dp[i + 1][j + 1] = dp[i + 1][j] | dp[i][j + 1] | dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
        return dp[n][m]
        