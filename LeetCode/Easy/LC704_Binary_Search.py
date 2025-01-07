class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # https://leetcode.com/problems/binary-search
        # 0ms 100%
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            num = nums[m]
            if target == num:
                return m
            elif target > num:
                l = m + 1
            else:
                r = m - 1
        return -1
