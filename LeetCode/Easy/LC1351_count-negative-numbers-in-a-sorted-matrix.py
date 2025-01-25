class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
        i = len(grid)-1
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            #print(i,j, grid[i][j])
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)        
