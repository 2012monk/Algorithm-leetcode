class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        
        def search(lo, hi):
            if lo == hi:
                return lo
            mid = (lo + hi) // 2
            nxt = mid + 1
            if A[mid] < A[nxt]:
                return search(nxt, hi)
            return search(lo, mid)
        return search(0, len(A) - 1)
            