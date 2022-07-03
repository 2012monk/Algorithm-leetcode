class Solution:
    def wiggleMaxLength(self, a: List[int]) -> int:
        
        p=[]
        for i in range(1, len(a)):
            if a[i] == a[i-1]:
                continue
            v=1
            if a[i]-a[i-1]<0:
                v=-1
            if not p or p[-1] != v:
                p.append(v)

        return len(p) + 1
                