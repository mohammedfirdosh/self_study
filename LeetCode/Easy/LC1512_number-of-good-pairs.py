class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/number-of-good-pairs/
        # 0ms 100%
        data_len = len(nums)
        pair_count = 0

        for l_ptr in range(data_len):
            r_ptr = data_len -1
            while l_ptr < r_ptr:
                if nums[l_ptr] == nums[r_ptr]:
                    pair_count += 1
                r_ptr -= 1
            

        
        return pair_count




        """
        # 0ms 100%
        dd = defaultdict(int)
        result = 0
        for num in nums:
            result += dd[num]
            dd[num] += 1
        return result
        """
