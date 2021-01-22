# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        result, bit = 0, 31 
        
        while n:
            result += (n&1) << bit
            n = n >> 1
            bit -= 1
        return result