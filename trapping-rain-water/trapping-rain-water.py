class Solution:
    def trap(self, H: List[int]) -> int:
        st = []
        r = 0
        for i in range(len(H)):
            
            while st and H[st[-1]] < H[i]:
                
                t = st.pop()
                
                if not st:
                    break
                
                d = i - st[-1] - 1
                v = min(H[i], H[st[-1]]) - H[t]
                r += d * v
            st.append(i)
                
                
        return r
                        
                    
                    
            
        