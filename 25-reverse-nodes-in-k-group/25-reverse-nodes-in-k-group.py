# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        node = head
        while node:
            tmp, count, st = node, 0, []
            for _ in range(k):
                if not tmp:
                    break
                st.append(tmp.val)
                tmp = tmp.next
                count += 1
            if count != k:
                break
                
            for _ in range(k):
                node.val = st.pop()
                node = node.next
        return head