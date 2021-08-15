/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode root = new ListNode();
        ListNode cur = root;
        
        while (head != null) {
            while (cur.next != null && cur.next.val < head.val) cur = cur.next;
            ListNode tmp = cur.next;
            cur.next = head;
            head = head.next;
            if (cur.next != null) cur.next.next = tmp;
            if (head != null && cur.val > head.val) cur = root;
        }
        return root.next;
        
    }
}