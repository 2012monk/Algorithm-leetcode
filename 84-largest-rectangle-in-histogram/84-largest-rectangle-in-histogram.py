class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        
        mx = -1
        s=[(-1,0)]
        for i,h in enumerate(hs):
            mx=max(mx, h)
            while s[-1][1] > h:
                lo,v = s.pop()
                mx = max(mx, (i-s[-1][0] - 1) * v)
            s.append((i, h))

        while s[-1][0] != -1:
            lo,v = s.pop()
            mx = max(mx, (len(hs) - s[-1][0] - 1) * v)
        return mx
