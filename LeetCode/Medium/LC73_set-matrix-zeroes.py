class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 73: https://leetcode.com/problems/set-matrix-zeroes/
        m = len(matrix)
        n = len(matrix[0])
        row_track = set()
        col_track = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    row_track.add(row)
                    col_track.add(col)
        for r_t in row_track:
            for col in range(n):
                matrix[r_t][col] = 0
        for c_t in col_track:
            for row in range(m):
                matrix[row][c_t] = 0
