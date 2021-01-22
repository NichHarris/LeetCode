# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        numMap = {}
                
        for i, val in enumerate(nums):
            if val not in numMap:
                numMap[val] = i
            
        for i in range(1, len(nums)+1):
            if i not in numMap:
                result.append(i)
                
        return result