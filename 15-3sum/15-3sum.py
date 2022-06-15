class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        r = set()
        a.sort()
        n = len(a)
        for i in range(n):
            target = -a[i]
            lo,hi = i + 1, n - 1
            if target < 0:
                break
            while lo < hi:
                cur = a[lo] + a[hi]
                if cur == target:
                    l = (a[i], a[lo], a[hi])
                    r.add(l)
                    while lo < hi and a[lo] == l[1]:
                        lo += 1
                    while lo < hi and a[hi] == l[2]:
                        hi -= 1
                    continue
                if cur < target:
                    lo += 1
                else:
                    hi -= 1
        return r
