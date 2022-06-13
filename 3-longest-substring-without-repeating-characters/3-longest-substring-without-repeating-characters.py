class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        t = [-1] * 128
        dp = [0] * len(s)
        dp[0] = 1
        t[ord(s[0])] = 0
        ret = 1
        for i in range(1, len(s)):
            c = s[i]
            idx = ord(c)
            if t[idx] == -1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = min(i - t[idx], dp[i - 1] + 1)
            t[idx] = i
            ret = max(ret, dp[i])
        return ret
        