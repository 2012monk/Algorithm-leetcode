class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ll = sorted(points, key=lambda x:(x[0]*x[0])+(x[1]*x[1]))
        return ll[:k]