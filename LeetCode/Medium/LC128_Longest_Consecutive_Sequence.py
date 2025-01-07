class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/longest-consecutive-sequence/
        # 40ms 86%
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num -1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max (longest, length)
        return longest
