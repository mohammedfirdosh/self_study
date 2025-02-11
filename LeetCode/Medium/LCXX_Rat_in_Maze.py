# Rat in maze
#User function Template for python3
class Solution:
    # Function to find all possible paths
    def __init__(self):
        print("In init")
    def findPath(self, mat):
        # code here
        print("In findPath()")
        num_row = num_col = len(mat)
        
        if mat[0][0] == 0 or mat[num_row -1][num_col-1] == 0:
            return []
            
        result = list()
        
        visitied_cell = [[False for _ in range(num_row)] for _ in range(num_col)]
        print(f"Initial visited cell: {visitied_cell}")
        def isSafe(r, c):
            if 0<= r < num_row and 0<=c < num_col and mat[r][c] == 1 and not visitied_cell[r][c]:
                return True
            return False
        
        
        def backtrack(r, c, path):
            if r == num_row -1 and c == num_col -1:
                result.append(path)
            visitied_cell[r][c] = True
            print("_"*40)
            #for row in visitied_cell:
            #    print(" ".join(map(str, row)))
            
            print(f"Path: {path} | Row= {r} | Col= {c}")
            # Left
            if isSafe(r, c-1):
                print("Left got added here")
                backtrack(r, c-1, path + 'L')
            
            # Right
            if isSafe(r, c+1):
                backtrack(r, c+1, path + 'R')

            # Up
            if isSafe(r-1, c):
                backtrack(r-1, c, path + 'U')
                
            # Down
            if isSafe(r+1, c):
                backtrack(r+1, c, path + 'D')
            
            visitied_cell[r][c] = False
                
        
        
        backtrack(r=0, c=0, path='')
        return sorted(result)


if __name__ == "__main__":

    mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    print(f"Matrix: {mat}")
    solution = Solution()
    result = solution.findPath(mat)
    if not result:
        print("[]")
    else:
        print(" ".join(result))
    print("~")
