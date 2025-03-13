# 350 https://leetcode.com/problems/intersection-of-two-arrays-ii
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h_map = {}
        for ii in nums1:
            if ii in h_map:
                h_map[ii] += 1
            else:
                h_map[ii] = 1
        
        result = []
        for num in nums2:
            if h_map.get(num, 0) > 0:
                result.append(num)
                h_map[num] -= 1
        return result
        """
        h_map = {ii: nums1.count(ii) for ii in nums1}

        result = []
        for num in nums2:
            if h_map.get(num, 0) > 0:
                result.append(num)
                h_map[num] -= 1
        return result
        """
