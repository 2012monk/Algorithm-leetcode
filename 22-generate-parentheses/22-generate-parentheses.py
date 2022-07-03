class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        r = set()
        a = [0] * (n * 2)
        m = n * 2
        def f(lo, hi, path):
            if len(path) == m:
                r.add(path)
                return
            if lo < n:
                f(lo+1,hi, path+'(')
            if hi < lo:
                f(lo,hi+1,path+')')


        f(0,0,'')
        return r
 