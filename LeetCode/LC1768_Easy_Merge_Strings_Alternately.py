class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        idx = 0
        merged_word = ''
        while idx < min_length:
            merged_word += word1[idx] + word2[idx]
            idx += 1
        if min_length == len(word1):
            merged_word += word2[idx:]
        else:
            merged_word += word1[idx:]
        return merged_word
