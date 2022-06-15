class Solution:
    def isValid(self, s: str) -> bool:
        
        m = {')': '(', ']': '[', '}': '{'}
        st = []
        for c in s:
            if c in (')', ']', '}'):
                if not st or st[-1] != m[c]:
                    return 0
                st.pop()
            else:
                st.append(c)
        print(st)
        return not st