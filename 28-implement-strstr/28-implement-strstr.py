class Solution:
    def strStr(self, h: str, e: str) -> int:
        def tb(s):
            t = [0]*len(s)
            j = 0
            for i in range(1, len(s)):
                while j>0 and s[i] != s[j]:
                    j = t[j - 1]
                if s[i] == s[j]:
                    j+=1
                    t[i] = j
            return t
        t = tb(e)
        j = 0
        m=len(e)
        for i in range(len(h)):
            while j > 0 and h[i] != e[j]:
                j =t[j - 1]
            if h[i] == e[j]:
                if j == m - 1:
                    return i-m+1
                j += 1
        return -1
        
        
        