class Solution:
    def trap(self, height: List[int]) -> int:
        total_water_collected = 0
        data_length = len(height)

        max_left_list = [0] * data_length
        max_right_list = [0] * data_length
        left_wall = right_wall = 0

        for l_ptr in range(data_length):
            r_ptr = -(l_ptr + 1)
            max_left_list[l_ptr] = left_wall
            max_right_list[r_ptr] = right_wall

            left_wall = max(left_wall, height[l_ptr])
            right_wall = max(right_wall, height[r_ptr])

        for idx in range(data_length):
            water_trapped = min(max_left_list[idx], max_right_list[idx]) - height[idx]
            if water_trapped > 0:
                total_water_collected += water_trapped
        
        return total_water_collected

