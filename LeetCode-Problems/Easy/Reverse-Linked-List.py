# Python

# Iterative
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        nxt = None
        while (current != None):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        
# Recursive
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(self, None, head)
    
    @staticmethod
    def reverse(self, previous, current):
        if (current == None):
            return previous
        nxt = current.next
        current.next = previous
        return self.reverse(self, current, nxt)
        
