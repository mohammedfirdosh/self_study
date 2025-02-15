# 37 https://leetcode.com/problems/sudoku-solver/
# TC: O(9 ** empty_cells)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        def is_safe(row, col, digit):
            # print(f"Check in row: {row} | Board {board[row]}")
            if digit in board[row]:
                return False

            # print("Check in column")
            for ii in range(9):
                if board[ii][col] == digit:
                    return False

            # print("Check in 3*3 grid")
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for ii in range(start_row, start_row + 3):
                for jj in range(start_col, start_col + 3):
                    if board[ii][jj] == digit:
                        return False
            # print(f"Digit: {digit} is safe to be placed on row: {row} and col: {col}")
            return True

        def backtrack(row, col):
            # Base condition. Exit if we have reached the last row
            if row == 9:
                return True
            # print(f"Working with row={row} and col={col} | Cell value: {board[row][col]}")

            # Move to next row if reached the last column
            next_row = row
            next_col = col + 1
            if next_col == 9:
                next_row = row + 1
                next_col = 0

            # Continue if the cell is already occupied
            if board[row][col] != ".":
                return backtrack(next_row, next_col)

            # Place the digit
            for digit in range(1, 10):
                # print(f"Trying to place digit: {digit}")
                if is_safe(row, col, str(digit)):
                    board[row][col] = str(digit)
                    if backtrack(next_row, next_col):
                        return True
                    # print("Backtrack/revert if the digit selected isn't appropriate")
                    board[row][col] = "."
            return False

        backtrack(0, 0)
