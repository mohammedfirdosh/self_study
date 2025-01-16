class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # https://leetcode.com/problems/excel-sheet-column-title
        # 0ms 100%
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(remainder + 65))
            columnNumber //= 26
        return ''.join(result[::-1])
