# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, n1, n2) -> ListNode:
        if n1 and n2:
            if n1.val > n2.val:
                n1, n2 = n2, n1
            n1.next = self.merge(n1.next, n2)
        return n1 or n2
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:
            return head
        h, s, f = None, head, head
        while f and f.next:
            h, s, f = s, s.next, f.next.next
        if h:
            h.next = None
        return self.merge(self.sortList(head), self.sortList(s))

            
                
                
            