# 367: https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num // 2 + 1

        while l <= r:
            m = l + (r - l) // 2
            calculated_square = m * m
            # print(f"left: {l}, right: {r}, mid: {m}, calculated_square: {calculated_square}")
            if num == calculated_square:
                return True
            elif num < calculated_square:
                r = m - 1
            else:
                l = m + 1
        return False
