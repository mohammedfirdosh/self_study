class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 342 https://leetcode.com/problems/power-of-four
        if n == 1:
            return True
        elif n == 0 or n % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(n // 4)
