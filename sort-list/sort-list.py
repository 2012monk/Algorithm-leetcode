# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            root = cur = ListNode()
            while node1 and node2:
                print(node1.val, node2.val)
                if node1.val < node2.val:
                    cur.next, node1 = node1, node1.next
                else:
                    cur.next, node2 = node2, node2.next
                cur = cur.next
                
            if node1:
                cur.next = node1
            if node2:
                cur.next = node2
            return root.next
        
        def sort(head):
            if not head or not head.next:
                return head
            root = head
            h, s, f = None, head, head
            while f and f.next:
                h, s, f = s, s.next, f.next.next
            if h:
                h.next = None
            return merge(sort(head), sort(s))
        
        res = c = sort(head)
        while c:
            print(c.val)
            c = c.next
            
        return res
            
                
                
            