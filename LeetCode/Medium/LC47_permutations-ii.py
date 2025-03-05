# 47 https://leetcode.com/problems/permutations-ii/?envType=problem-list-v2&envId=backtracking
# https://www.youtube.com/watch?v=cvOVk7kuMYg
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx == n:
                result.append(nums[:])
                return

            unique_set = set()
            for i in range(idx, n):
                if nums[i] in unique_set:
                    continue
                unique_set.add(nums[i])
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        n = len(nums)
        result = list()
        backtrack(0)
        return result
