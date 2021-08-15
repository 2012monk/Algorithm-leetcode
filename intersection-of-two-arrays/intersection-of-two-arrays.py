class Solution:
    def search(self, a, t):
        l,r = 0,len(a)-1
        while l <= r:
            m = (l+r)//2
            if a[m] == t:
                return m
            if a[m] > t:
                r = m - 1
            else:
                l = m + 1
        return -1
        
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        # n1,n2 = sorted(list(set(n1))), sorted(list(set(n2)))
        # if len(n1) > len(n2):
        #     n1, n2 = n2, n1
        # res = set()
        # for k in set(n1):
        #     i = bisect.bisect_left(n2, k)
        #     if 0 <= i < len(n2):
        #         res.add(k)
        # return list(res)
        n1, n2 = set(n1), set(n2)
        res =[]
        if len(n1) > len(n2):
            n1,n2=n2,n1
        return [k for k in n1 if k in n2]