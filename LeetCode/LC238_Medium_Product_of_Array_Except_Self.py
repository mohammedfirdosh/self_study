class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 13ms Beats 97.88%
        zero_count = nums.count(0)
        product = math.prod([num for num in nums if num != 0])
        result = [0]*len(nums)
        if zero_count > 1:
            return result
        elif zero_count == 1:
            result[nums.index(0)] = product
            return result
        else:
            return [product//element for element in nums]

    """
        27ms Beats 49.14%

        l_mult = r_mult = 1
        data_len = len(nums)
        l_arr = [0] * data_len
        r_arr = [0] * data_len

        for ll in range(data_len):
            rr = -ll -1
            l_arr[ll] = l_mult
            r_arr[rr] = r_mult

            l_mult *= nums[ll]
            r_mult *= nums[rr]
        
        return [ll*rr for ll, rr in zip(l_arr, r_arr)]
    """
    """
        178ms Beats 5.00%

        #return [math.prod(nums[:ii] + nums[ii+1:]) for ii in range(len(nums))]

        n=len(nums)
        a=[1]*n
        for i in range(n-2, -1, -1):
            a[i]=nums[i+1]*a[i+1]
        b=1
        for j in range(1,n):
            b*=nums[j-1]
            a[j]*=b
        return a
    """    
        
