# 81 https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        s, e = 0, n - 1

        while s <= e:
            m = s + (e - s) // 2
            #print(f"s: {s}, e: {e}, m: {m}", end="|")
            if target == nums[m]:
                #print("Found element")
                return True

            if nums[s] == nums[m]:
                s += 1
                continue

            if nums[e] >= nums[m]:
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1
            else:
                if nums[s] <= target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
        return False
