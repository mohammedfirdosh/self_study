class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        #https://leetcode.com/problems/self-dividing-numbers

        #4ms 83%
        result = list()
        for num in range(left, right+1):
            if num % 10 == 0:
                continue
            tmp = num
            while tmp >= 1:
                digit = tmp % 10
                if digit == 0 or num % digit != 0:
                    break
                tmp //= 10
            else:
                result.append(num)
        
        return result
