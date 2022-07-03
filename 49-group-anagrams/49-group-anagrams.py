class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def h(s):
            return ''.join(sorted(list(s)))
        m=defaultdict(list)
        for s in strs:
            m[h(s)].append(s)
        return m.values()