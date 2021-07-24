# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        root = even = ListNode(0)
        origin = ListNode(0)
        origin.next = head
        while head:
            t = head.next
            if not t:
                even.next = None
                break
            head.next = t.next
            even.next = t

            head = head.next
            even = even.next
            
        c = origin.next
        while c and c.next:
            c = c.next
        
        if c:
            c.next= root.next
        return origin.next