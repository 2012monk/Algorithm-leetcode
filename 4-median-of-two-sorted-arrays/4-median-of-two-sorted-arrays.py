class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        
        a = [0] * (len(a1) + len(a2))
        j,k = 0, 0
        for i in range(len(a)):
            if j >= len(a1):
                a[i] = a2[k]
                k += 1
                continue
            elif k >= len(a2):
                a[i] = a1[j]
                j += 1
                continue
                
            if a1[j] > a2[k]:
                a[i] = a2[k]
                k += 1
            else:
                a[i] = a1[j]
                j += 1
        print(a)
        mid = a[len(a) // 2]
        if len(a) % 2 == 0:
            mid = (mid + a[len(a) // 2 - 1]) / 2
        return mid