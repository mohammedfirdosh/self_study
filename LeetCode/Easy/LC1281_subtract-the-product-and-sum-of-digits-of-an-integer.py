class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
        prod_of_digits = 1
        sum_of_digits = 0
        while n >= 1:
            digit = n % 10
            prod_of_digits *= digit
            sum_of_digits += digit
            n //= 10
        return prod_of_digits - sum_of_digits
