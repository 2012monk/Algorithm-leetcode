class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        count = Counter(s)
        
        b = [0 for _ in range(26)]
        for c in s:
            count[c] -= 1
            i = ord(c) - 97
            if b[i] == 1:
                continue
                
            while st and count[st[-1]] > 0 and st[-1] > c:
                b[ord(st.pop()) - 97] = 0
            st.append(c)
            b[i] = 1
                
            
        return ''.join(st)
            
            