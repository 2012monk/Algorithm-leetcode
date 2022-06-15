t ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        i = 0
        n = len(s)
        while i < n:
            r = t[s[i]]
            if s[i] == 'I' and i < n - 1 and s[i + 1] in ('V', 'X'):
                r = t[s[i + 1]] - r
                i += 1
            if s[i] == 'X' and i < n - 1 and s[i + 1] in ('L', 'C'):
                r = t[s[i + 1]] - r
                i += 1
            if s[i] == 'C' and i < n - 1 and s[i + 1] in ('D', 'M'):
                r = t[s[i + 1]] - r
                i += 1
            ret += r
            i += 1
        return ret
