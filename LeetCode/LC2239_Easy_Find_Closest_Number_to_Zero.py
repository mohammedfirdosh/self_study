class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums = list(map(abs, nums))
        nums.sort()
        return nums[0]
        
