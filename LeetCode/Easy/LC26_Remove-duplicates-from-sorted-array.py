class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array
        # 0ms 100%
        ptr = 1
        data_length = len(nums)
        for idx in range(1, data_length):
            if nums[idx - 1] != nums[idx]:
                nums[ptr] = nums[idx]
                ptr += 1

        return ptr  
