# 374 : https://leetcode.com/problems/guess-number-higher-or-lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        lowerBound, upperBound = 1, n
        # Binary division faster than (lowerBound + upperBound) //2
        myGuess = (lowerBound+upperBound) >> 1
        # walrus operator ':=' - assigns value of the function to the variable 'res'
        # and then compare res with 0
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess+1
            else:
                upperBound = myGuess-1
            myGuess = (lowerBound+upperBound) >> 1

        return myGuess

    """
        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m - 1
    """
