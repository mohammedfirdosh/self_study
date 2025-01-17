class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # https://leetcode.com/problems/special-positions-in-a-binary-matrix

        # 3ms 67%
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        # Populate the count arrays
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Identify and count special positions
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1

        return special_count
