# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = collections.deque()
        
        root = cur = ListNode(0)
        idx = 0
        
        lists = sorted(list(filter(lambda x: x is not None, lists)), key=lambda x: x.val)
        if not lists:
            return None
        
        while lists:
            cur.next = lists[0]
            lists[0] = lists[0].next
            cur = cur.next
            lists = sorted(list(filter(lambda x: x is not None, lists)), key=lambda x: x.val)
            
        return root.next
            
        
        
                
        
        
        
        
        