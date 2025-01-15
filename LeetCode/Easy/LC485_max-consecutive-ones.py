class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/max-consecutive-ones
        # 8ms 92%
        result, current_max = 0, 0

        for num in nums:
            if num:
                current_max += 1
            else:
                result = max (result, current_max)
                current_max = 0 

        return  max (result, current_max)
