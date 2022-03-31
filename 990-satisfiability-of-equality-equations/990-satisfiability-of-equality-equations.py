import collections
import sys

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        sys.setrecursionlimit(100000)
        graph = {x: x for x in 'abcdefghijklmnopqrstuvwxyz'}
        def find(x):
            if x != graph[x]:
                graph[x] = find(graph[x])
            return graph[x]
        for e in equations:
            if e[1] != '=':
                continue
            graph[find(e[0])] = find(e[3])
        for e in equations:
            if e[1] != '!':
                continue
            if find(e[0]) == find(e[3]):
                return False
        return True
            