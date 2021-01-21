# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        numMap = {1000: "M",
                  900: "CM",
                  500: "D",
                  400: "CD",
                  100: "C",
                  90: "XC",
                  50: "L",
                  40: "XL",
                  10: "X",
                  9: "IX",
                  5: "V",
                  4: "IV",
                  1: "I"}
        temp = num
        result = ""
        i = 0
        while temp > 0:
            if (temp - numList[i]) >= 0:
                result += numMap[numList[i]]
                temp -= numList[i]
            else:
                i += 1
        
        return result