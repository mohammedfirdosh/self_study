# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # https://leetcode.com/problems/first-bad-version
        # 28ms 92.59%
        result = n
        start_ptr, end_ptr = 1, n
        while start_ptr <= end_ptr:
            mid_ptr = (start_ptr + end_ptr) // 2          
            if isBadVersion(mid_ptr):
                result = mid_ptr
                end_ptr = mid_ptr -1
            else:
                start_ptr = mid_ptr + 1

        return start_ptr
