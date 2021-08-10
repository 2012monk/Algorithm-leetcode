# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, arr, t):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r)//2
            if arr[m] <= t:
                r = m - 1
            else:
                l = m + 1
        return arr[l]
                
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = (len(nums) + 1) // 2
        def build(arr):
            if not arr:
                return
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = (len(arr) - 1) // 2
            node = TreeNode(arr[mid])
            
            node.left = build(arr[:mid])
            node.right = build(arr[mid+1:])
            return node
        return build(nums)
        
            