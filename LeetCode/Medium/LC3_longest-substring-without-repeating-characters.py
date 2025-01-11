class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # https://leetcode.com/problems/longest-substring-without-repeating-characters
        # 10ms 96%
        char_map = dict()
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
            #print(f"char_map: {char_map} | max_length: {max_length} | start: {start} | end: {end}")
        return max_length
