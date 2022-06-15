class Node:
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.word = 0
        self.root = 0
    
    def add(self, s, i):
        if i == len(s):
            self.word = 1
            return
        if s[i] not in self.children:
            self.children[s[i]] = Node(s[i])
        self.children[s[i]].add(s, i + 1)
    def query(self):
        if len(self.children) != 1 or self.word:
            return self.c
        res = [n.query() for n in self.children.values()]
        if not res:
            return ''
        return self.c + max(res, key=lambda x: len(x))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Node('')
        trie.root = 1
        for s in strs:
            trie.add(s, 0)
            if not s:
                return ""
        return trie.query()
