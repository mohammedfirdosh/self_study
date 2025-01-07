class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/majority-element/

        # 0ms 100% 19.35MB 17.71%
        majority = len(nums) // 2
        nums.sort()
        return nums[majority]

        """
        data_dict = defaultdict(int)
        for num in nums:
            data_dict[num] += 1
        majority = len(nums) // 2
        for kk, vv in data_dict.items():
            if vv > majority:
                return kk
        """
