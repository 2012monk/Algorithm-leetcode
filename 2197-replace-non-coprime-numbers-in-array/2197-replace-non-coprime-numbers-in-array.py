import collections
class Solution:
    def isCoprime(self, n1, n2):
        return math.gcd(n1, n2) == 1
    def isHaveNonCoprime(self, arr):
        for i in range(len(arr) - 1):
            if not self.isCoprime(arr[i], arr[i + 1]):
                return True
        return False
            
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for n in nums:
            st.append(n)
            while len(st) > 1 and gcd(st[-1], st[-2]) != 1:
                st.append(lcm(st.pop(), st.pop()))
        return st
