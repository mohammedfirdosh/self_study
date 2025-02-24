# 334 https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            print(f"INT: {first}, {second}, {num}")
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                print(f"TRUE: {first}, {second}, {num}")
                return True
        print(f"FALSE: {first}, {second}, {num}")
        return False
        """
        n = len(nums)
        if n < 3:
            return False
        p1, p2, p3 = 0, 1, 2
        while p3 < n:
            print(f"Comparing: {nums[p1]} < {nums[p2]} < {nums[p3]} at index {p1}, {p2} & {p3}")
            if nums[p1] < nums[p2] < nums[p3]:
                return True
            p1 += 1
            p2 += 1
            p3 += 1
        return False
        """
