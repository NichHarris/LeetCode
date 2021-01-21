# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i = 0
        j = 0
        for idx in range(len(nums1)):
            if j >= n or (i < m and temp[i] <= nums2[j]):
                nums1[idx] = temp[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1