class Solution:
    def canJump(self, a: List[int]) -> bool:
        
            
        n=len(a)
        last=n-1
        for i in range(n-2,-1,-1):
            if i+a[i]>=last:
                last = i
        return last<=0