# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        group = 1
        node = head
        while node:
            st = []
            tmp,count = node, 0
            for _ in range(group):
                if not tmp:
                    break
                st.append(tmp.val)
                tmp = tmp.next
                count+=1
            group += 1
            if count & 1:
                node = tmp
                continue
            for _ in range(count):
                node.val = st.pop()
                node = node.next
        return head