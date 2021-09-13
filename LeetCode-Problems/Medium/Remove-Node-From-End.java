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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = 0;
        ListNode curr = head;
        
        while (curr != null){
            curr = curr.next;
            len++;
        }
        
        int pointer = 0;
        curr = head;
        if (len - n == 0){
            return head.next;
        }
        while (pointer < (len - n) - 1){
            curr = curr.next;
            pointer++;
        }
        curr.next = curr.next.next;
        return head;
        
    }
}
