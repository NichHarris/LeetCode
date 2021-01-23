# https://leetcode.com/problems/palindrome-linked-list/

class Solution(object):
    
    def isEqual(self, head, rev):
        while (head != None and rev != None):
            if (head.val != rev.val):
                return False
            head = head.next
            rev= rev.next
        return (head == None and rev == None)
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        
        if head == None or head.next == None:
            return head
        
        rev = ListNode()
        rev = self.isPalindrome(head.next)
        
        return self.isEqual(head,rev)