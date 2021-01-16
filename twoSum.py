class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in hashMap:
                return [hashMap[complement], i]
            
            hashMap[val] = i
        return []