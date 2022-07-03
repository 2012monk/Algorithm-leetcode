class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
                
                
        n = len(a)
        i=0
        while i < n:
            v=a[i]
            if v<0 or v >= n or v == i + 1 or v ==a[v - 1]:
                i += 1
            else:
                a[i],a[v-1]=a[v-1],a[i]
        for i in range(n):
            if a[i] != i + 1:
                return i + 1
        return n+1
            
            
            
            
