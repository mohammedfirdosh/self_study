class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # https://leetcode.com/problems/merge-sorted-array
        mp = m -1
        np = n - 1
        tp = m + n -1 

        while np >= 0:
            if mp >= 0 and nums1[mp] > nums2[np]:
                nums1[tp] = nums1[mp]
                mp -= 1
            else:
                nums1[tp] = nums2[np]
                np -= 1
            tp -= 1                
