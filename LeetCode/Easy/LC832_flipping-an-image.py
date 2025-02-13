class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/flipping-an-image
        for row in image:
            l, r = 0, len(row) - 1
            while l <= r:
                row[l], row[r] = row[r]^1, row[l]^1
                r -= 1
                l += 1
        return image
