class Solution:
    def sumZero(self, n: int) -> List[int]:
        # https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
        return [(ii*2-n+1) for ii in range(n)]
