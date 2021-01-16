class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        buy = prices[0]
        profit = 0
        
        for i in prices[1:]:
            if i-buy > profit:
                profit = i -buy
                
            if i < buy:
                buy = i
        return profit