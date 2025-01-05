class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)
        if w1_len == 0:
            return word2
        if w2_len == 0:
            return word1
        result = ''.join(f"{w1}{w2}" for w1,w2 in zip(word1, word2))
        if w1_len == w2_len:
            return result
        if w1_len > w2_len:
            result = f"{result}{word1[-(w1_len - w2_len):]}"
        elif w1_len < w2_len:
            result = f"{result}{word2[-(w2_len - w1_len):]}"       

        return result
        
