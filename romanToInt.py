# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numMap = {"M": 1000,
                  "CM": 900,
                  "D": 500,
                  "CD": 400,
                  "C": 100,
                  "XC": 90,
                  "L": 50,
                  "XL": 40,
                  "X": 10,
                  "IX": 9,
                  "V": 5,
                  "IV": 4,
                  "I": 1}
        
        result = 0
        i = 0
        
        while i < len(s):
            num = numMap[s[i]]
            if i < len(s)-1 and s[i:i+2] in numMap:
                num = numMap[s[i:i+2]]
                i += 1
            result += num
            i += 1
        return result