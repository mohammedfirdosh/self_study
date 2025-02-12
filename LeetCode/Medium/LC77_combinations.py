# 77 https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res, sol = list(), list()

        def backtrack(x):
            #print(f"sol: {sol} | ", end=" ")
            if len(sol) == k:
                res.append(sol[:])
                #print(f"In res: {res}")
                return

            left = x
            still_need = k - len(sol)

            if left > still_need:
                backtrack(x - 1)

            #print(f"Out res: {res}")
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res
