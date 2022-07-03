class Solution:
    def wiggleMaxLength(self, a: List[int]) -> int:
        
        p=[]
        mx=0
        for i in range(1, len(a)):
            if a[i] == a[i-1]:
                continue
            c = a[i]-a[i-1]
            v=1
            if c<0:
                v=-1
            if not p or p[-1] != v:
                p.append(v)

        return len(p) + 1
                