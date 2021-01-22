# https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)           
        for i in range(1, num+1):
            counter = 0
            n = i
            while n != 0:
                counter += 1
                n &= (n-1)
            result[i] = counter 
        
        return result