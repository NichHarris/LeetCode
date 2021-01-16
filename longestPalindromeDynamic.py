class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ""
        
        for i in range(len(s)):
            for j in range(len(s),i, -1): # len(s) - 1 = j, from len(s) to i
                if len(palindrome) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]: # Check if current substring is a palindrome
                    palindrome = s[i:j]
                    break
        return palindrome