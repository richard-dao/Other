# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while (curr != None):
            curr = curr.next
            l = l + 1
            
        if (l == n):
            return head.next
        p = 0
        curr = head
        while (p < (l - n) - 1):
            curr = curr.next
            p = p + 1
        
        curr.next = curr.next.next
        return head
