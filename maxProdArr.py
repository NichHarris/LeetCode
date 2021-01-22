# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = currMin = nums[0]
        result = currMax
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            tempMax = max(num, currMax*num, currMin*num)
            currMin = min(num, currMax*num, currMin*num)
            currMax = tempMax
            
            # Choose the max between previous product and newly calculated product
            result = max(currMax, result)
        return result