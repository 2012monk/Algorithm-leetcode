class Trie {
    
    static class TrieNode {
        Map<String, TrieNode> children;
        boolean word;
        public TrieNode() {
            this.word = false;
            this.children = new HashMap<>();
        }
    }
    TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        this.root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = this.root;
        for (String s: word.split("")) {
            node.children.put(s, node.children.getOrDefault(s, new TrieNode()));
            node = node.children.get(s);
        }
        node.word = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = this.root;
        for (String s: word.split("")) {
            if (!node.children.containsKey(s)) {
                return false;
            }
            node = node.children.get(s);
        }
        return node.word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode node = this.root;
        for (String s: prefix.split("")) {
            if (!node.children.containsKey(s)) {
                return false;
            }
            node = node.children.get(s);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */