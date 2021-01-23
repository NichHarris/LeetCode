# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {")": "(", "}": "{", "]": "["}
                
        for char in s:
            if char in matching:
                top = stack.pop() if stack else '#'
                if matching[char] != top:
                    return False
            else:
                stack.append(char)  
        return not stack