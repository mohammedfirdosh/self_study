# 128 https://leetcode.com/problems/longest-consecutive-sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map = {ii: False for ii in nums}
        global_long = 0

        for k, v in h_map.items():

            local_long = 0
            if v:
                continue
            t = k
            while t in h_map and h_map[t] == False:
                h_map[t] = True
                local_long += 1
                # print(f"First loop: with t: {t}, h_map: {h_map}| local_long: {local_long}")
                t += 1
            t = k - 1
            while t in h_map and h_map[t] == False:
                h_map[t] = True
                local_long += 1
                # print(f"Second loop: with t: {t}, h_map: {h_map}| local_long: {local_long}")
                t -= 1
            global_long = max(global_long, local_long)
            # print(f"Finished with k: {k}| Global long: {global_long}")

        return global_long


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/longest-consecutive-sequence/
        # 40ms 86%
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num -1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max (longest, length)
        return longest
"""
