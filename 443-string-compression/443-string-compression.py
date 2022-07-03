class Solution:
    def compress(self, a: List[str]) -> int:
        

        i=0
        index=0
        while i<len(a):
            c=0
            x=a[i]
            while i<len(a) and x==a[i]:
                i+=1
                c+=1
            a[index]=x
            index+=1
            if c==1:
                continue
            for d in list(str(c)):
                a[index] = str(d)
                index+=1
            
                

        return index