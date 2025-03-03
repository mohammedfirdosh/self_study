# 2161 https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2025-03-03
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #"""
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        # First pass: Place elements less than pivot
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1
        
        # Second pass: Place elements greater than pivot
        for num in reversed(nums):
            if num > pivot:
                result[right] = num
                right -= 1
        
        # Third pass: Place pivot elements in the middle
        for num in nums:
            if num == pivot:
                result[left] = num
                left += 1
        
        return result
        #"""
        """
        less, equal, greater = list(), list(), list()
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return less + equal + greater
        """
