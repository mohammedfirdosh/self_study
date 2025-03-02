# 131 https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        def backtrack(s, start, path, result):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, n):
                if is_palindrome(s, start, end):
                    path.append(s[start : end + 1])
                    backtrack(s, end + 1, path, result)
                    path.pop()

        n = len(s)
        res = list()
        backtrack(s, 0, [], res)
        return res
