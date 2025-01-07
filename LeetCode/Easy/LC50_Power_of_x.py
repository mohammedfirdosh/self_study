class Solution:
    def myPow(self, x: float, n: int) -> float:

        # https://leetcode.com/problems/powx-n

        # 0ms 100%
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f


        """
        # 3ms 7.32%
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2

        return result        
        """
