# Greedy Algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        result = nums[0]
        
        for i in range(1,len(nums)):
            current = max(nums[i], current + nums[i])
            result = max(result, current)
        return result



# Dynamic
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i -1]
            
            result = max(nums[i], result)
        return result