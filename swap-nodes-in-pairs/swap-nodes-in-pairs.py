# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = cur = ListNode(0)
        cur.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            
            cur.next = tmp
            
            head, cur = head.next, cur.next.next
            
        return root.next