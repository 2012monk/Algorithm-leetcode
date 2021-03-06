# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, cur = None, slow.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        slow.next=  None
        
        h1, h2 = head, prev
        while h2:
            h1.next, h1, h2 = h2, h2, h1.next