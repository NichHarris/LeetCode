class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == s[::-1]:
            return s
        
        longestSub = s[0]
        newSub = ''
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                right = i + 1
                left = i
                while right < len(s)  and left >= 0 and s[left] == s[right]:
                    newSub = s[left:right+1]
                    right += 1
                    left -= 1
                if len(newSub) > len(longestSub):
                    longestSub = newSub
        
        for j in range(1, len(s)-1):
            right = j + 1
            left = j - 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                newSub = s[left:right+1]
                right += 1
                left -= 1
            if len(newSub) > len(longestSub):
                longestSub = newSub
        
        return longestSub