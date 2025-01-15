class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-greatest-common-divisor-of-array
        # 0ms 100%
        min_num = min(nums)
        max_num = max(nums)

        while min_num:
            max_num, min_num = min_num, max_num % min_num
        return max_num
        
