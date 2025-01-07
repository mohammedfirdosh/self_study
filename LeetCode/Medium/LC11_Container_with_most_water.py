class Solution:
    def maxArea(self, height: List[int]) -> int:

        # 102ms 54%
        # https://leetcode.com/problems/container-with-most-water/
        l_ptr, r_ptr = 0, len(height)-1
        max_area = 0
        while l_ptr < r_ptr:
            max_area = max (max_area, min(height[l_ptr], height[r_ptr]) * (r_ptr - l_ptr))
            #print(f"BEFORE: l_ptr: {l_ptr} | r_ptr: {r_ptr} | max_area: {max_area}")
            if height[l_ptr] > height[r_ptr]:
                r_ptr -= 1
            else:
                l_ptr += 1
            #print(f"AFTER: l_ptr: {l_ptr} | r_ptr: {r_ptr}")
        
        #print(f"FINAL: max_area: {max_area}")
        return max_area
        

