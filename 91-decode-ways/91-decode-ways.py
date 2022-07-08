class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        d = [0] * (n + 2)
        d[n] = d[n + 1] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            d[i]+=d[i + 1]
            if i + 1  < n and int(s[i] + s[i+1]) <= 26:
                d[i] += d[i + 2]

        
        print(d)
        return d[0]