class Solution:
    def search(self, a: List[int], t: int) -> int:
            
        def bs(l, r):
            if l > r:
                return -1
            if a[l] > t and a[r] < t:
                return -1

            mid = (l+r)//2
            if a[mid] == t:
                return mid
            left = bs(l, mid - 1)
            right = bs(mid + 1, r)
            
            if left == -1 and right == -1:
                return -1
            if left != -1:
                return left
            if right != -1:
                return right
                
        
        return bs(0, len(a) - 1)
            
            
            