class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(bin(n))
        # if n < 0:
        #     n = ~n
        print(n)
        if n == 0:
            return False
        r = 0
        for _ in range(33):
            r += n&1
            n>>=1
        return r <= 1