# 633 https://leetcode.com/problems/sum-of-square-numbers/?envType=problem-list-v2&envId=binary-search
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))

        while a <= b:
            sum_of_square = a * a + b * b
            # print(f"a={a}, b={b}, c={c}, sum_of_square: {sum_of_square}")

            if sum_of_square == c:
                return True
            elif sum_of_square < c:
                a += 1
            else:
                b -= 1
        return False
