class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-number/

        #0ms 100%
        result = 0
        for num in nums:
            result ^= num
        return result
