class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


        # 48ms 83%
        count = {}
        k = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] <= 2:
                nums[k] = num
                k += 1
        return k

        """
        51ms 67%

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
        """
