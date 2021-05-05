//Java
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
    public ListNode middleNode(ListNode head) {
        ListNode current = head;
        int leng = 0;
        while (current != null){
            leng++;
            current = current.next;
        }
        current = head;
        int x = 0;
        while (x < leng/2){
            current = current.next;
            x++;
        }
        return current;   
    }
}
