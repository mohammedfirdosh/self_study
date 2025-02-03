class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-three
        if n in [1, 3]:
            return True
        elif n in [0,2] or n % 3 != 0:
            return False
        else:
            return self.isPowerOfThree(n //3)




        """
        if n == 0:
            return False
        
        while n % 3 == 0:
            n /= 3
        return True if n == 1 else False
        """
