"""
Step by Step Algorithm
Initialization:

Initialize an empty list res to store the subsets.
Initialize an empty list subset to temporarily store subsets during recursion.
res = []
subset = []
Define Recursive Function:

Define a recursive function create_subset that takes an index i as its parameter.
If the index i reaches the length of the input list nums, add the current subset to the result res.
Otherwise, for each element in nums, include it in the subset and recursively call create_subset with the next index (i+1).
After the recursive call, remove the last element from the subset to backtrack, and recursively call create_subset with the same index (i+1).
"""
# 78 https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = list(), list()

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res
