class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://leetcode.com/problems/search-a-2d-matrix
        #0ms 100%
        m = len(matrix)
        n = len(matrix[0])

        for rr in range(m):
            if matrix[rr][0] <= target <= matrix[rr][-1]:
                s, e = 0, n - 1
                while s <= e:
                    m = (s + e) // 2
                    if matrix[rr][m] == target:
                        return True
                    elif matrix[rr][m] > target:
                        e = m - 1
                    else:
                        s = m + 1
        return False
