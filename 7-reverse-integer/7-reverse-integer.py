class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        ret = int(str(x)[::-1])
        ret *= sign
        if ret < MIN or ret > MAX:
            return 0
        return ret