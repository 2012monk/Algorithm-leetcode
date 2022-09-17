class Solution:
    def calculate(self, s: str) -> int:
        st = []
        ret, n, sign = 0,0,1
        
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c in ('-', '+'):
                ret += sign * n
                n = 0
                sign = (-1, 1)[c == '+']
            elif c == '(':
                st.append(ret)
                st.append(sign)
                ret,sign = 0, 1
            elif c == ')':
                ret += sign * n
                ret *= st.pop()
                ret += st.pop()
                n = 0
        return ret + sign * n
                
                
            
                