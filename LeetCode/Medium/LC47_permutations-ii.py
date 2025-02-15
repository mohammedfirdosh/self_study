# 47 https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        h_map = {ii: nums.count(ii) for ii in nums}
        n = len(nums)
        sol = list()

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for elem in h_map:
                if h_map[elem] > 0:
                    sol.append(elem)
                    h_map[elem] -= 1
                    backtrack()

                    h_map[elem] += 1
                    sol.pop()

        backtrack()
        return res
