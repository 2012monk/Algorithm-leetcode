class Solution:
    def pointer(self, n, t):
        l, r = 0, len(n) - 1
        while l != r:
            if n[l] + n[r] < t:
                l += 1
            elif n[l] + n[r] > t:
                r -= 1
            else:
                return l+1, r+1
            
    def twoSum(self, n: List[int], t: int) -> List[int]:
        # return self.pointer(n, t)
        for i, k in enumerate(n):
            v = t - k
            j = bisect.bisect_left(n, v, i + 1)
            if j < len(n) and n[j] == v:
                return i + 1, j + 1
        return []