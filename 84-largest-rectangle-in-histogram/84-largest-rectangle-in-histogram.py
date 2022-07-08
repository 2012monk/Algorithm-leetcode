class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        
        mx = -1
        s=[-1]
        n=len(hs)
        for i in range(n):
            while s[-1] != -1 and hs[s[-1]] >= hs[i]:
                v = hs[s.pop()]
                mx = max(mx, (i-s[-1] - 1) * v)
            s.append(i)

        while s[-1] != -1:
            v = hs[s.pop()]
            mx = max(mx, (n - s[-1] - 1) * v)
        return mx
