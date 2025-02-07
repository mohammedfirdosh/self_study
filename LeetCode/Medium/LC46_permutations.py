"""
Algorithm :
Base Case:
If the current index reaches the length of the array, add the current permutation to the result.


Recursive Swapping:
Iterate over the array starting from the current index.
Swap the current index with the iteration index.
Recurse for the next index.
Backtrack by swapping the elements back to restore the array.

"""
# 46: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                helper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        result = list()
        helper(0)
        return result

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res, sol = list(), list()

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
"""
