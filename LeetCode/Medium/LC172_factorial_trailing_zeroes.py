class Solution:
    def trailingZeroes(self, n: int) -> int:

        """
        To find the number of trailing zeroes in ( n! ) (n factorial), you need to count the number of times 10 is a factor in the numbers from 1 to ( n ). Since 10 is the product of 2 and 5, and there are usually more factors of 2 than 5, the number of trailing zeroes is determined by the number of times 5 is a factor.
        """
        # https://leetcode.com/problems/factorial-trailing-zeroes
        # 0% 100%
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count        
