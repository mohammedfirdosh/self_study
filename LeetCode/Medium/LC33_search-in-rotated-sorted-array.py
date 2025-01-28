class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #https://leetcode.com/problems/search-in-rotated-sorted-array
        data_len = len(nums)
        l, r = 0, data_len - 1
        while l <= r:
            m = (l + r)//2
            #print(l, r, m)
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m +1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1 
        return -1        
