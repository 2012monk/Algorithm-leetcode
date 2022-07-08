class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        d = [0] * (n + 2)
        d[-1] = d[-2] = 1
        if s[-1] == '*':
            d[n-1]=9
        elif s[-1] != '0':
            d[n-1] = 1

        for i in range(n-2, -1, -1):
            if s[i] == '0':
                continue
            if s[i] == '*':
                d[i] += d[i+1]*9
            else:
                d[i]+=d[i+1]
            if s[i] == '*':
                if s[i + 1] == '*':
                    d[i] += d[i+2] * 15
                elif int(s[i+1])<7:
                    d[i] += d[i+2]*2
                else:
                    d[i] += d[i+2]
                d[i]%=mod
                continue    
            if s[i+1] == '*':
                if s[i] == '1':
                    d[i] += d[i+2]*9
                if s[i] == '2':
                    d[i] += d[i+2]*6
            elif (ord(s[i])-48)*10 + ord(s[i+1])-48<=26:
                d[i]+=d[i+2]
            d[i]%=mod
            
        return d[0]%mod