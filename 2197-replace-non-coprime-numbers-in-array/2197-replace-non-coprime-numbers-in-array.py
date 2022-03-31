import collections
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for n in nums:
            st.append(n)
            while len(st) > 1 and gcd(st[-1], st[-2]) != 1:
                st.append(lcm(st.pop(), st.pop()))
        return st
