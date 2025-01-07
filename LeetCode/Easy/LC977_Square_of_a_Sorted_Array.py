class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/squares-of-a-sorted-array/


        # 0ms 100%
        n = len(nums)
        L, R = 0, n-1
        result = []

        for i in range(n):
            nums[i] = nums[i] ** 2

        while L <= R:
            if nums[L] > nums[R]:
                result.append(nums[L])
                L += 1
            else:
                result.append(nums[R])
                R -= 1

        result.reverse()
        return result

        """
        # 0ms, 100%
        return sorted(num**2 for num in nums)
        """
