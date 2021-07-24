# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, l: int, r: int) -> ListNode:
        if l == r:
            return head
        root = start = ListNode(0)
        root.next = head
        
        for _ in range(l - 1):
            start = start.next
        end = start.next
        
        for _ in range(r - l):
            t, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = t
            
        return root.next
        