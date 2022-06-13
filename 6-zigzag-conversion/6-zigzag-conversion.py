class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows < 2:
            return s
        n = len(s)
        m = [[]  for _ in range(n)]

        r = 0
        b = 1
        for i in range(n):
            m[r].append(s[i])
            r += b
            if r >= numRows:
                r -= 2
                b = -1
            if r < 0:
                r += 2
                b = 1

        ret = ""
        for p in m:
            ret += "".join(p)
        return ret
