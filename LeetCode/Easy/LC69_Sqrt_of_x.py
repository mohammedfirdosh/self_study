class Solution:
    def mySqrt(self, x: int) -> int:
        # https://leetcode.com/problems/sqrtx
        
        # 2ms 67%
        # Newton-Rapson Method
        if x < 2:
            return x

        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2

        return guess

        """
        # 7ms 30%
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1

        return right     
        """   
