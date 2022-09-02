class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        d = defaultdict(list)
        @lru_cache(maxsize=None)
        def comb(w):
            ret = []
            for i in range(len(w)):
                ret.append(w[:i] + "*" + w[i + 1:])
            return ret
        for w in wordList:
            for c in comb(w):
                d[c].append(w)

        def bfs(s, e):
            q = deque([(s, 1)])
            v = set([s])
            while q:
                cur, cnt = q.popleft()
                if cur == e:
                    return cnt
                for w in comb(cur):
                    for nxt in d[w]:
                        if nxt in v:
                            continue
                        v.add(nxt)
                        q.append((nxt, cnt + 1))
            return 0
        return bfs(beginWord, endWord)

                