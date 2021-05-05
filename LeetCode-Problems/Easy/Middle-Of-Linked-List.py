# Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        leng = 0
        while(current != None):
            leng = leng + 1
            current = current.next
        current = head
        x = 0
        while (x < leng/2):
            current = current.next
            x = x+1
        return current
