class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-peak-element
        data_len = len(nums)
        if data_len == 1:
            return 0
        if data_len == 2:
            return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return data_len -1

        s, e = 0, data_len - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            if m == data_len -1 and nums[m] > nums[m - 1]:           
                return m
            if m == 0 and nums[m] > nums[m + 1]:
                return m
            if nums[m] < nums[m + 1]:
                s = m + 1
            else:
                e = m - 1
