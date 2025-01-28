class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
        def helper(searching_left):
            idx = -1
            data_len = len(nums)
            l, r = 0, data_len - 1

            while l <= r:
                m = (l + r) // 2
                #print(f"searching_left: {searching_left} | ", l, r, m, f"idx: {idx}")
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    idx = m
                    if searching_left:
                        r = m -1 
                    else:
                        l = m + 1
            return idx

        left = helper(searching_left=True)
        right = helper(searching_left=False)
        return [left, right]
