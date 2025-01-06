class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 0ms Beats 100.00%
        
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            # If the current number is not consecutive, end the current range
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        
        # Add the last range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges
