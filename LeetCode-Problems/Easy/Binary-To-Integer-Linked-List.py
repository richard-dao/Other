# Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count = ""
        current = head
        while(current != None):
            count += str(current.val)
            current = current.next
        return int(count, 2)
