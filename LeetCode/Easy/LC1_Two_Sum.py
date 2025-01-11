class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/two-sum
        # 0ms 100%
        num_to_index = dict()

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], idx]
            num_to_index[num] = idx
        return []
