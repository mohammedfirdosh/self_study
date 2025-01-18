class Solution:
    def hammingWeight(self, n: int) -> int:
        #https://leetcode.com/problems/number-of-1-bits
        
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count        
