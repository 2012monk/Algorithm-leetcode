class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st, count = [], Counter(s)
        for c in s:
            count[c] -= 1
            if c in st:
                continue
            while st and count[st[-1]] > 0 and st[-1] > c:
                st.pop()
            st.append(c)
            
        return ''.join(st)
            
            