class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = set()
        
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            
            hashMap.add(nums[i])
            if len(hashMap) > k:
                hashMap.remove(nums[i-k])
        
        return False