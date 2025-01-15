class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/four-divisors/

        total_sum = 0
        for num in nums:
            divisor = set()
            for ii in range(1, int(num ** 0.5) + 1):
                if num % ii == 0:
                    divisor.add(num//ii)
                    divisor.add(ii)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                total_sum += sum(divisor)

        return total_sum        

        """
        # 125ms 88%
        total_sum = 0
        for num in nums:
            divisor_count = 0
            current_sum = 0
            for ii in range(1, int(num ** 0.5) + 1):
                if num % ii == 0:
                    divisor_count += 1
                    current_sum += ii
                    if ii != num // ii:
                        divisor_count += 1
                        current_sum += num // ii
                    if divisor_count > 4:
                        break
            if divisor_count == 4:
                total_sum += current_sum

        return total_sum
        """
