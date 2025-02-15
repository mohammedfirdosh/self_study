# 51 https://leetcode.com/problems/n-queens
# TC: O(n!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def is_safe(row, col):
            # Check the row
            for jj in range(col):
                if board[row][jj] == "Q":
                    return False

            # Check the column
            for ii in range(row):
                if board[ii][col] == "Q":
                    return False

            # Check the main diagonal (top-left to bottom-right)
            for ii, jj in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[ii][jj] == "Q":
                    return False

            # Check the secondary diagonal (top-right to bottom-left)
            for ii, jj in zip(range(row, -1, -1), range(col, n)):
                if board[ii][jj] == "Q":
                    return False

            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return res
