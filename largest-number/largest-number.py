class Solution:
    def less(self, i, j, n):
        a, b = n[i], n[j]
        if int(str(a)+str(b)) < int(str(b) + str(a)):
            # n[i], n[j] = n[j], n[i]
            return True
        return False
        
    def largestNumber(self, n: List[int]) -> str:

        for i in range(len(n)):
            j = i - 1
            while j >= 0 and self.less(j, j+1, n):
                n[j + 1],n[j] = n[j],n[j+1]
                j -= 1

            
        return str(int(''.join(list(map(str, n)))))