# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = ListNode(0)
        current = output
        carry  = 0
        sum = 0           
        while l1 or l2 or carry:
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            sum = carry + x + y
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            sum %= 10    
            
            current.next = ListNode(sum)
            current = current.next
            if l1:
                l1 = (l1.next if l1 else None)
            if l2:
                l2 = (l2.next if l2 else None)
        
        return output.next