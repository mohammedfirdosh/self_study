class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #https://leetcode.com/problems/rearrange-array-elements-by-sign

        # 31ms 98%
        result = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2

        return result

        """
        # 42ms 75%
        positive_num_array = [num for num in nums if num >= 0]
        negative_num_array = [num for num in nums if num < 0]
        result_array = list()
        for idx in range(len(positive_num_array)):
            result_array.append(positive_num_array[idx])
            result_array.append(negative_num_array[idx])
        return result_array
        """
