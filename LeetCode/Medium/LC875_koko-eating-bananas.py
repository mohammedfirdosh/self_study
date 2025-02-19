# 875 https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = ceil(sum(piles) / h), max(piles)
        while s < e:
            m = s + (e - s) // 2
            time_taken = 0
            for p in piles:
                if time_taken > h:
                    break
                time_taken += ceil(p / m)
            if time_taken <= h:
                e = m
            else:
                s = m + 1

        return e
