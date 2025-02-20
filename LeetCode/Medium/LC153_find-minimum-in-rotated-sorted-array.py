# 153 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=problem-list-v2&envId=binary-search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        s, e = 0, n - 1
        while s < e:
            m = s + (e - s) // 2
            if nums[m] > nums[e]:
                s = m + 1
            else:
                e = m
        return nums[s]

        """
        n = len(nums)
        s, e = 0, n - 1
        current_min = float('-inf')
        while s < e:
            m = s + (e - s) // 2
            print(f"s: {s}, e: {e}, m: {m}", end="|")
            if current_min == float('-inf'):
                current_min = nums[m]
            else:
                current_min = min(current_min, nums[m])
            print(f"Current min with mid: {current_min}")
            if nums[s] < nums[m]:
                print("Left sorted", end='|')
                if current_min == float('-inf'):
                    curremt_min = nums[s]
                else:
                    current_min = min(current_min, nums[s])
                print(f"current_min: {current_min}")
            else:
                print("Left not sorted", end='|')
                e = m - 1
                print("Continue after moving end pointer")

            if nums[m] < nums[e]:
                print("Right sorted", end='|')
                if current_min == float('-inf'):
                    curremt_min = nums[m]
                else:
                    current_min = min(current_min, nums[m])
                print(f"current_min: {current_min}")  
            else:
                print("Right not sorted", end='|')
                s = m + 1
                print("Continue after moving start pointer")


        return current_min

        """
