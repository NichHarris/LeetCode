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
        # Linked List is empty or of size 1, no operations needed
        if head == None or head.next == None:
            return head
        
        result = ListNode()
        result = self.reverseList(head.next)
        
        
        head.next.next = head
        head.next = None
        return result