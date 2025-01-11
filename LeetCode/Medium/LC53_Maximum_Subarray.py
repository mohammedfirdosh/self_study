class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-subarray
        max_so_far = nums[0]
        max_ending_here = nums[0]

        data_len = len(nums)
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far
