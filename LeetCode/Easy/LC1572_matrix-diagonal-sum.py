class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # https://leetcode.com/problems/matrix-diagonal-sum/

        #0ms 100%
        primary_diagonal_sum = 0
        secondary_diagonal_sum = 0
        n = len(mat)
        for ii in range(n):
            primary_diagonal_sum += mat[ii][ii]
            secondary_diagonal_sum += mat[ii][n - ii -1]
        if n % 2 == 0:
            return primary_diagonal_sum + secondary_diagonal_sum
        else:
            return primary_diagonal_sum + secondary_diagonal_sum - mat[n//2][n//2]
