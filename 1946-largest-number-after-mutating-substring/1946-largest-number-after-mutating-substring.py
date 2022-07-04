class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        n = len(num)
        d = [0] * n
        a = list(num)
        ret = 0
        flag = 0
        for i in range(n):
            v=int(num[i])
            c=change[v]
            if c < v and flag:
                break

            if c > v:
                a[i] = str(c)
                flag = 1

            

            

            
        return ''.join(a)
