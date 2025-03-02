#2596: https://leetcode.com/problems/check-knight-tour-configuration
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def is_valid(r, c, n, exp_val):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != exp_val:
                return False

            if exp_val == n * n - 1:
                return True

            ans1 = is_valid(r - 2, c - 1, n, exp_val + 1)
            ans2 = is_valid(r - 2, c + 1, n, exp_val + 1)
            ans3 = is_valid(r - 1, c - 2, n, exp_val + 1)
            ans4 = is_valid(r - 1, c + 2, n, exp_val + 1)
            ans5 = is_valid(r + 1, c - 2, n, exp_val + 1)
            ans6 = is_valid(r + 1, c + 2, n, exp_val + 1)
            ans7 = is_valid(r + 2, c - 1, n, exp_val + 1)
            ans8 = is_valid(r + 2, c + 1, n, exp_val + 1)

            return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8

        n = len(grid)
        return is_valid(0, 0, n, 0)
