class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        vi = set()
        traced = set()
        for k, v in prerequisites:
            g[k].append(v)
        
        def dfs(i):
            if i in traced:
                return False

            if i in vi:
                return True
            
            traced.add(i)
            for k in g[i]:
                if not dfs(k):
                    return False
            vi.add(i)
            traced.remove(i)
            return True
        
        for x in list(g):
            if not dfs(x):
                return False
        return True
        