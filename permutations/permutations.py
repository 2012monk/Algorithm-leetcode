sys.setrecursionlimit(int(1e9))
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = []
        
        def search(li):
            if len(li) == 0:
                result.append(prev[:])
                
            for n in li:
                nxt = li[:]
                nxt.remove(n)
                
                prev.append(n)
                search(nxt)
                prev.pop()
            
        search(nums)
            
            
        return result
            
            