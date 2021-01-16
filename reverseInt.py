class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31:
            return 0 
        else:
            strR = str(x)
            if x >= 0:
                revst = strR[::-1]
            else:
                temp = strR[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31-1:
            return 0
        else:
            return int(revst)