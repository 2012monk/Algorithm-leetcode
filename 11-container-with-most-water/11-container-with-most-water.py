class Solution:
    def maxArea(self, a: List[int]) -> int:
        lo,hi = 0, len(a) - 1
        ret = 0
        while lo < hi:
            ret = max(ret, (hi - lo) * min(a[hi], a[lo]))
            if a[lo] < a[hi]:
                lo += 1
            else:
                hi -= 1
        return ret
        