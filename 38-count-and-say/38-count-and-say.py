class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return '1'
        r = ''
        p = self.countAndSay(n-1)
        i=0
        while i < len(p):
            x = p[i]
            k=1
            i+=1
            while i<len(p) and p[i]==x:
                i+=1
                k+=1
            r += str(k)+x
        return r
            
            