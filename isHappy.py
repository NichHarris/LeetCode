# https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def getNext(n):
            total = 0
            while n > 0:
                n, digit = divmod(n,10)
                total += digit ** 2
            return total
        
        mapping = {}
        
        while n != 1 and n not in mapping:
            mapping[n] = n
            n = getNext(n)
        
        return n == 1