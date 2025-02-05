class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 35: https://leetcode.com/problems/search-insert-position
        data_len = len(nums)
        l, r = 0, data_len - 1

        while l <= r:
            m = (l + r) // 2
            #print("in: ", l, r, m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        #print("out: ", l, r, m)
        return l


        """
        
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        
        for idx in range(len(nums)):
            print(f"List element: {nums[idx]} at index {idx} with target element: {target}")
            if target == nums[idx]:
                return idx
            elif nums[idx] < target < nums[idx+1]:
                return idx + 1
            elif nums[idx] > target:
                return idx
        """
