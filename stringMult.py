# https://leetcode.com/problems/multiply-strings/submissions/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = int(num1)*int(num2)
        return str(product)

# OR 
# # https://leetcode.com/problems/multiply-strings/submissions/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # product = int(num1)*int(num2)
        # return str(product)
        
        numbers = { "0": 0,
                    "1": 1,
                    "2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9}
        
        num1Int = num2Int = i = j = 0
        
        for char in num1:
            if (len(num1) - i) == 1:
                num1Int += numbers[char]
            else:
                num1Int += numbers[char]*pow(10,(len(num1)-1-i))
            i += 1
        for char in num2:
            if (len(num2) - j) == 1:
                num2Int += numbers[char]
            else:
                num2Int += numbers[char]*pow(10,(len(num2)-1-j))
            j += 1
                   
        return str(num1Int*num2Int) 