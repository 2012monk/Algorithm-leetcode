class Solution:
    def _pow(self, x, n):
        ret = 1
        while n:
            if n & 1:
                ret *= x
            x *= x
            n //= 2 
        return ret
    def r_pow(self, x, n):
        ret = 1
        while n:
            if n & 1:
                ret /= x
            x /= x
            n //= 2 
        return ret

    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return self._pow(x, n)
        return self._pow(1/x, -n)
        
        