# 1732: https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude

        """
        n = len(gain)
        result = [0] * (n + 1)
        for ii in range(n):
            result[ii + 1] = result[ii] + gain[ii]
        return max(result)
        """
