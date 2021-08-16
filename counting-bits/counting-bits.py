class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0, 1, 1]
        if n < 3:
            return table[:n+1]
        c = 1
        for i in range(3, n+1):
            if i > (1 << c):
                c += 1
            k = 1 << c
            
            # print(k)
            if not i^k:
                table.append(1)
            else:
                table.append(table[i-k]+1)
        
        return table