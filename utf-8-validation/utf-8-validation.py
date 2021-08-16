class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(st, size):
            for i in range(st + 1, st+size + 1):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True

        
        l = len(data)
        i = 0
        while i < l:
            s = data[i]
            if s >> 3 == 0b11110 and check(i, 3):
                i += 4
            elif s >> 4 == 0b1110 and check(i, 2):
                i += 3
            elif s >> 5 == 0b110 and check(i, 1):
                i += 2
            elif s >> 7 == 0:
                i += 1
            else:
                return False
            
        return True
        
            
        