class Solution:
    def numberOfMatches(self, n: int) -> int:
        # https://leetcode.com/problems/count-of-matches-in-tournament/

        # Brainless approach / Smart solution
        return n - 1

        """
        # Iterative approach
        total_matches = 0
        while n > 1:
            matches = n // 2
            total_matches += matches
            n = matches + (n % 2)
        return total_matches
        """
