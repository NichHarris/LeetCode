# https://leetcode.com/problems/sum-of-two-integers/

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # Use bit manip
        
        x, y = abs(a), abs(b)
        
        if x < y:
            return self.getSum(b,a)
        
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            while y:
                # x^y = XOR
                # << 1 lEFT SHIFTED BY 1
                x, y = x^y, (x&y) << 1
        else:
            while y:
                x, y = x^ y, ((~x)&y) << 1
        
        return x*sign