# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search   
        start, end = 0, len(nums) -1
        
        if len(nums) == 1 or nums[end] > nums[0]:
            return nums[0]
        
        while start <= end:
            mid = start + (end- start)/2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid -1