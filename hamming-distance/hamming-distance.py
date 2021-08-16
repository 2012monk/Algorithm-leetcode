class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = bin(x^y)[2:]
        return s.count('1')