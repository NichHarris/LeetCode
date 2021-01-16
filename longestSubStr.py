class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {}
        length = 0
        j = 0
        for i in range(len(s)):
            if s[i] in hashMap:
                j = max(j, hashMap[s[i]] + 1)
            
            length = max(length, i - j + 1)
            hashMap[s[i]] = i
        return length