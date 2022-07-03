class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        def f(a, b):
            s = 1
            if a< 0:
                a = -a
                s=-s
            if b<0:
                b = -b
                s=-s
            if b > a:
                return 0
            q = f(a, b * 2)
            if a - 2*q*b < b:
                return s*(q+q)
            return s*(q+q+1)
        mx = (1<<31)-1
        mn = -(1<<31)
        r=f(dividend, divisor)
        if r >= mx:
            return mx
        if r <= mn:
            return mn
        return r