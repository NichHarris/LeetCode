class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = ""
        
        for i in range(1, min(len(str1), len(str2)) + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                root = str1[:i]
                mult1 = len(str1)/i
                mult2 = len(str2)/i
                
                if root*mult1 == str1 and root*mult2 == str2:
                    gcd = root
        return gcd