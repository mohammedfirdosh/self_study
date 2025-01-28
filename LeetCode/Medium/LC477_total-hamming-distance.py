class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/total-hamming-distance
        result = 0
        for bit in range(32):
            #print('*'*40)
            one_count = 0
            zero_count = 0
            mask = 1 << bit
            for num in nums:
                t = num & mask
                #print(f"Debugging: bit = {bit} | num = {num} ({bin(num)}), mask = {bin(mask)} |  t = {t} ({bin(t)})" )
                if t:
                    one_count += 1
                else:
                    zero_count += 1
            result += one_count*zero_count
        return result
