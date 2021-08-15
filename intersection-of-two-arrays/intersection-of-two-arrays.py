class Solution:
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        n1, n2 = set(n1), set(n2)
        if len(n1) > len(n2):
            n1,n2=n2,n1
        return [k for k in n1 if k in n2]