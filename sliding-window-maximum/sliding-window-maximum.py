class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:

        res = []
        if not n:
            return res
        d = deque()
        
        for i in range(len(n)):
            
            while d and d[0] < i - k + 1:
                d.popleft()
            while d and n[d[-1]] < n[i]:
                d.pop()
            d.append(i)
            if i >= k - 1:
                res.append(n[d[0]])
        return res
            
            
            
            
            