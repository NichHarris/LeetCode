# https://leetcode.com/problems/partition-list/solution/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)
        
        while head != None:
        
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
        
            # Move head to next element
            head = head.next
        
        # End the after List
        after.next = None
        
        # Combine the two lists, from the end of the before list, to the node after the head of the after list
        # Head node of after is 0 (set at start)
        before.next = afterHead.next
        
        return beforeHead.next