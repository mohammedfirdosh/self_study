# 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        n = len(digits)
        res, sol = [], []
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i == n:
                res.append("".join(sol))
                return

            for letter in letter_map[digits[i]]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res
