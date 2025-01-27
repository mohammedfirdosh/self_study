class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-element-in-a-sorted-array
        data_len = len(nums)
        if data_len == 1:
            return nums[0]

        s, e = 0, data_len - 1

        while s <= e:
            m = (s + e) // 2
            #print(f"{s}, {e}, {m} | {nums[m - 1]}, {nums[m]}, {nums[m + 1]}", end="  ")
            #print(f"{s}, {e}, {m}", end=' ')
            if m == data_len - 1:
                if nums[m - 1] != nums[m]:
                    return nums[m]
            elif nums[m - 1] != nums[m] and nums[m] != nums[m + 1]:
                return nums[m]
            if m % 2 == 0 and nums[m] == nums[m + 1]:
                #print("cond1")
                s = m + 1
            elif m % 2 == 0 and nums[m] != nums[m + 1]:
                #print("cond2")
                e = m - 1
            elif m % 2 != 0 and nums[m - 1] == nums[m]:
                #print("cond3")
                s = m + 1
            elif m % 2 != 0 and nums[m - 1] != nums[m]:
                #print("cond4")
                e = m - 1
