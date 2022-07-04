class Solution:
    def candy(self, a: List[int]) -> int:
        
        n = len(a)
        if n <= 1:
            return n
        d = [1] * n
        for i in range(1, n):
            if a[i] >a[i-1]:
                d[i] = d[i-1]+  1
        
        for i in range(n - 1, 0, -1):
            if a[i - 1] > a[i]:
                d[i - 1] = max(d[i -1], d[i] + 1)
        return sum(d)
            
            
            