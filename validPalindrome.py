class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                left, right = s[:l] + s[l+1:], s[:r] + s[r+1:]
                return left == left[::-1] or right == right[::-1]
            l += 1
            r -= 1
        return True
        
        
        # OR       
        
        
        def isPaliRange(i,j):
            return all(s[k] == s[j-k+i] for k in range(i,j))
        
        for i in range(len(s)/2):
            if s[i] != s[~i]:
                j = len(s) - 1 -i
                return isPaliRange(i+1,j) or isPaliRange(i,j-1)
        return True