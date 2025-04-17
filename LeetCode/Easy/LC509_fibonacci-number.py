# LC 509: https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        def foo(n):
            if dp[n] == -1:
                if n in [0,1]:
                    dp[n] = n
                if n - 2 >= 0:
                    dp[1] = 1
                    dp[n] = foo(n - 1) + foo(n - 2)

            return dp[n]

        dp = [-1] * (n + 1)
        foo(n)
        return dp[n]


"""
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
"""
