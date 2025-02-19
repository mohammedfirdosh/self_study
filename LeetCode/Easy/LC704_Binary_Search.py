class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def bs(start, end):
            if end < start:
                return -1
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return bs(start, mid - 1)
            else:
                return bs(mid + 1, end)

        return bs(0, n - 1)

        """
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
        """
