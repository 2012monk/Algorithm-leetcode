sys.setrecursionlimit(10**6)

#class Solution:
#    def isMatch(self, s: str, p: str) -> bool:
#        
#        n,m=len(s),len(p)
#        dp = {}
#        def f(i, j):
#            if j == m:
#                dp[i,j] = i == n
#                return dp[i, j]
#            if (i, j) in dp:
#                return dp[i, j]
#            match = i < n and p[j] in ('.', s[i])
#            if j < m - 1 and p[j + 1] == '*':
#                dp[i,j] = f(i, j + 2) or match and f(i + 1, j)
#            else:
#                dp[i,j] = f(i + 1, j + 1) and match
#            return dp[i,j]
#        return f(0, 0)
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)