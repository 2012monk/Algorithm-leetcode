class Solution:
    def calculate(self, s: str) -> int:
        
        numbers = '0123456789'
        op = {'+': 0, '-': 0, '*': 1, '/': 1}
        arr = []
        t = ''
        for c in s:
            if c in numbers:
                t += c
            if c in op:
                arr.append(t)
                arr.append(c)
                t = ''
        arr.append(t) 
        a = []
        st = []
        for c in arr:
            if c not in op:
                a.append(c)
                continue
            while st and op[st[-1]] >= op[c]:
                a.append(st.pop())
            st.append(c)
        while st:
            a.append(st.pop())
            
        st = []
        for c in a:
            if c not in op:
                st.append(int(c))
                continue
            b = st.pop()
            a = st.pop()
            if c == '+':
                st.append(a+b)
            if c == '-':
                st.append(a-b)
            if c == '*':
                st.append(a*b)
            if c == '/':
                st.append(a//b)
        return st[0]
                
