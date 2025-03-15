# LC 2062 https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        n = len(word)

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] in vowels:
                    seen.add(word[j])
                    if len(seen) == 5:
                        count += 1
                else:
                    break
        return count
