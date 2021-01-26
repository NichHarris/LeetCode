# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
                
        line = 0
        pos = 0
        outputArr = [""]*numRows
        
        for i in s:
            outputArr[line] += i
            if line == 0 or line == numRows - 1:
                pos ^= 1
            line += 1 if pos else -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outputArr[j]
        return outputStr