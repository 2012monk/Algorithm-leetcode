class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        h = []
        for p in people:
            heapq.heappush(h, [-p[0], p[1]])
        res = []
        while h:
            p = heapq.heappop(h)
            res.insert(p[1], [-p[0], p[1]])
        return res
        
        