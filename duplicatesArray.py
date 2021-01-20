class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashMap = {}
        result = []
        for i, val in enumerate(nums):
            if val in hashMap:
                result.append(val)
            hashMap[val] = i
            
        return result