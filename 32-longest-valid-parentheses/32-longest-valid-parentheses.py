class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        st = []
        
        d = [0] * len(s)
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                st.append(i)
                continue
            if st and s[st[-1]] == '(':
                st.pop()
            else:
                st.append(i)
        if not st:
            ans = len(s)
        
        prev = len(s)
        while st:
            cur = st.pop()
            ans = max(ans, prev - cur - 1)
            prev = cur
        ans = max(ans, prev)
        return ans

