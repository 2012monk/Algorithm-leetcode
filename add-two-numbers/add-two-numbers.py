# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        d = 1
        res = None
        s = 0
        while l1 or l2:
            if l1:
                s += d * l1.val
                l1 = l1.next
            if l2:
                s += d * l2.val
                l2 = l2.next
            d *= 10
        print(s)
        for i in str(s):
            node = ListNode(i)
            node.next,res = res, node
        return res
            
            
        