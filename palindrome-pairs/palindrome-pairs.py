class Node:
    def __init__(self):
        self.children = defaultdict(Node);
        self.w = []
        self.wid = -1
        
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def isPal(word):
        return word[::] == word[::-1]

    def insert(self, idx, word):
        node = self.root
        for i, char in enumerate(word[::-1]):
            if self.isPal(word[0:len(word)-i]):
                node.w.append(idx)
            node = node.children[char]
        node.wid = idx
        
    def search(self, idx, word):
        res = []
        node = self.root
        while word:
            if node.wid >= 0 and self.isPal(word):
                res.append([idx, node.wid])
                
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]
            
        if node.wid >= 0 and node.wid != idx:
            res.append([idx, node.wid])
            
        for p in node.w:
            res.append([idx, p])
        return res
        
        
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for i, w in enumerate(words):
            trie.insert(i, w)
        res = []
        for i, word in enumerate(words):
            res.extend(trie.search(i, word))
        return res
        
        
            
        