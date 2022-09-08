class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        def search(lo, hi):
            if lo == hi:
                return lo
            mid = (lo + hi) // 2
            nxt = mid + 1
            if max(mat[mid]) < max(mat[nxt]):
                return search(nxt, hi)
            return search(lo, mid)
        i = search(0, len(mat) - 1)
        return [i, mat[i].index(max(mat[i]))]
        
        
                
