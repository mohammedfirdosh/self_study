# 264 https://leetcode.com/problems/ugly-number-ii/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(n: int) -> bool:
            if n <= 0:
                return False
            for p in [2, 3, 5]:
                while n % p == 0:
                    n //= p
            return n == 1

        count = 0
        num = 1
        while count < n:
            if isUgly(num):
                count += 1
            num += 1
        return num - 1
