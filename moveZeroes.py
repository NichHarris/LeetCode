# https://leetcode.com/problems/move-zeroes/solution/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] == 0:
                nums.append(0)    
                nums.remove(0)
                j -= 1
            else:
                i += 1