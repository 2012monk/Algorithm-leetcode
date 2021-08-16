class Solution:
    def hammingWeight(self, n: int) -> int:
        int_max = 0x7f_ff_ff_ff
        r = 0
        for i in range(33):
            r += (n & (1 << i))//(1<<i)
        return r