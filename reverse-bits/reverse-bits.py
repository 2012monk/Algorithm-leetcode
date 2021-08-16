class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(31,-1,-1):
            # print(i, end=' ')
            r |= (n&1) << i
            # print(bin(r))
            n>>=1
        return r