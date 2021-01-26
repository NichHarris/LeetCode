class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        
        result = [-1,-1]
        
        left = right = 0
        
        while right < len(nums):
            if nums[left] != target:
                left += 1
                right += 1
            elif nums[right] == target:
                result = [left, right]
                right += 1
            else:
                break
        return result