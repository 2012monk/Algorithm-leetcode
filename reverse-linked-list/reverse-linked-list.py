# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        res = dummy
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
        