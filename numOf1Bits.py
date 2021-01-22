# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        
        while n != 0:
            counter += 1
            # 101 & 100 = 100, i = 1 -> 100 & 99 = 00, i = 2 -> end
            # 11011 & 11010 = 11010, i = 1 -> 11010 & 11009 = 11000, i = 2 -> 11000 & 10999 = 10000, i = 3 -> 10000 & 9999 = 0, i = 4 -> end
            n &= (n-1)
            
        return counter