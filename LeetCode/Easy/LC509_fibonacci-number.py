class Solution:
    def fib(self, n: int) -> int:
        # 509 https://leetcode.com/problems/fibonacci-number
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        elif n == 3:
            return 2
        else:
            return self.fib(n - 1) + self.fib(n - 2)
