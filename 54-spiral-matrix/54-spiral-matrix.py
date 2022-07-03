class Solution:
    def spiralOrder(self, g: List[List[int]]) -> List[int]:
        
        
        m,n=len(g),len(g[0])
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        i,j=0,0
        c=0
        t=m*n
        dr=0
        ret=[]
        
        while c < t:
            ret.append(g[i][j])
            g[i][j] = -101
            x,y=i+d[dr][0],j+d[dr][1]
            if x < 0 or x >=m or y<0 or y>=n or g[x][y] == -101:
                dr = (dr+1) % 4
            i,j=i+d[dr][0],j+d[dr][1]
            c+=1
        return ret
        
            
            
            
