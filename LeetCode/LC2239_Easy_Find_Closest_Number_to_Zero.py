class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for element in nums:
            if abs(element) < abs(closest):
                closest = element
        if abs(closest) in nums and closest < 0:
            return abs(closest)
        return closest
        
