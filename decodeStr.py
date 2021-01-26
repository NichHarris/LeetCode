# https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
class Solution:
    def decodeString(self, s):
        
        left = 0
        output = ""
        stack = [""]
        num_stack = []
        while left < len(s):
            if s[left].isdigit():       
                digit = ""
                # Convert the string to int as it can double digits
                while s[left].isdigit():
                    digit += s[left]
                    left += 1
                
                digit_int = int(digit)
                stack.append("")
                num_stack.append(digit_int)                
            elif s[left] == ']':                    
                mul_string = num_stack.pop()
                top_str = stack.pop()                    
                stack[-1] += mul_string * top_str
            else:
                stack[-1] += s[left]
            left += 1       
            
            
            
        
        return stack[0]