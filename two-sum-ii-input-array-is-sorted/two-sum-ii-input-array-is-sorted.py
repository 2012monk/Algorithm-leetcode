class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i, k in enumerate(n):
            v = t - k
            j = bisect.bisect_left(n, v, i + 1)
            if j < len(n) and n[j] == v:
                return i + 1, j + 1
        return []