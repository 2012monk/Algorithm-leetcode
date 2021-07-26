class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        st = []
        b = [0] * len(T)
        
        for i, v in enumerate(T):
            
            while st and T[st[-1]] < v:
                l = st.pop()
                b[l] = i - l
            st.append(i)
        return b
            
            
                
            
        