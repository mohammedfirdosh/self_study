# 338 https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits_of_1(num):
            num_of_1 = 0
            while num >= 1:
                num_of_1 += num % 2
                num //= 2
            return num_of_1

        return [count_bits_of_1(ii) for ii in range(n + 1)]
