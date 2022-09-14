class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        m = defaultdict(int)
        
        for c in s:
            m[c] += 1
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1