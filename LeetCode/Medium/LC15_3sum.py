# 15 https://leetcode.com/problems/3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res



        """
        # Sort and 2 pointer approach
        n = len(nums)
        result = set()
        nums.sort()
        # nums   = [-1,0,1,2,-1,-4]
        # sorted = [-4,-1,-1,0,1,2]

        for ii in range(n):
            first_num = nums[ii]
            l, r = ii + 1, n - 1
            while l < r:
                second_num = nums[l]
                third_num = nums[r]
                total = first_num + second_num + third_num
                if total == 0:
                    result.add((first_num, second_num, third_num))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return list(result)
        """

        """
        # Approach similar to 2SUM
        n = len(nums)
        result = set()
        for ii in range(n):
            target = -nums[ii]
            ss = set()
            for jj in range(ii+1, n):
                to_find = target-nums[jj]
                if to_find not in ss:
                    
                    ss.add(nums[jj])
                else:
                    #response = {nums[ii], nums[jj], to_find}
                    #result.add(response)
                    tt = [nums[ii], nums[jj], to_find]
                    tt.sort()
                    result.add((tt))
        return list(result)



        """

        """
        # Brute force - 308 / 313 testcases passed
        n = len(nums)
        result = set()
        for ii in range(n):
            for jj in range(ii + 1, n):
                for kk in range(jj + 1, n):
                    if nums[ii] + nums[jj] + nums[kk] == 0:
                        result.add((nums[ii], nums[jj], nums[kk]))

        return list(result)
        """
