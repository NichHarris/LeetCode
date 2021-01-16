class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return str(x) == str(x)[::-1]
        count = 0
        inp = list(str(x))
        inv = inp[::-1]
        for i in range(len(inp)):
            if inp[i] == inv[i]:
                count += 1
                #if len(inp)/2 == i:
                #    return True
            else:
                return False
                break   
        if len(inp) == count:
            return True