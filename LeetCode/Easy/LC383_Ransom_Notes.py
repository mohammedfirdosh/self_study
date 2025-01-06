class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 3ms Beats 97.91%
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True

        """
        # 13ms Beats 81.53%

        ransomNote_map = {}
        for character in ransomNote:
            if character in ransomNote_map:
                ransomNote_map[character] += 1
            else:
                ransomNote_map[character] = 1
            if character not in magazine:
                return False
        #print(f"BEFORE: ransomNote_map: {ransomNote_map}")
        for character in magazine:
            if character in ransomNote_map:
                ransomNote_map[character] -= 1
        
        #print(f"AFTER: ransomNote_map: {ransomNote_map}")
        #print(list(val <= 0 for val in ransomNote_map.values()))
        return all(val <= 0 for val in ransomNote_map.values())
        """
