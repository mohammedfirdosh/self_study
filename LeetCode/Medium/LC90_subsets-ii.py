# 90: https://leetcode.com/problems/subsets-ii/
# https://www.youtube.com/watch?v=pNzljlzDCiI&list=PLfqMhTWNBTe2C_dQAP1UoemcgAxBTlItp&index=3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == n:
                result.append(sol[:])
                return

            # Inclusion
            sol.append(nums[i])
            backtrack(i + 1)

            # Exclusion
            # Exclude all the equal elements
            idx = i + 1
            while idx < n and nums[idx - 1] == nums[idx]:
                idx += 1
            sol.pop()
            backtrack(idx)

        nums.sort()
        n = len(nums)
        result, sol = list(), list()
        backtrack(0)
        return result
