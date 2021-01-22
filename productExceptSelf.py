# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [0]*len(nums)
        result[0] = 1
        
        for i in range(1, len(nums)):
            result[i] = nums[i-1]*result[i-1]
        
        revRes = 1
        for i in reversed(range(len(nums))):
            result[i] = result[i]*revRes
            revRes *= nums[i]
        
        return result