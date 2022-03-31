# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count != k:
            return head
        
        cur = self.reverseKGroup(cur, k)
        while count:
            head.next,cur, head = cur, head, head.next
            count -= 1
        return cur