class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        
        if not a:
            return 0
        u={}
        ans=0
        for i in a:
            if i in u:
                continue
            left=u.get(i-1, 0)
            right=u.get(i+1,0)
            s=left+right+1
            u[i]=s
            ans=max(ans, s)
            
            u[i-left]=s
            u[right + i]=s
        return ans
