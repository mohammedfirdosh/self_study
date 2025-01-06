class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 0ms Beats 100.00%
        char_count = {c: text.count(c) for c in 'balloon'}
        char_count['l'] //= 2
        char_count['o'] //= 2
        return min(char_count.values())

        """
        # 3ms Beats 61.65%
        expected_hash_map = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        obtained_hash_map = {}
        for char in set('balloon'):
            char_count = text.count(char)
            if 'balloon'.count(char) > char_count:
                return 0
            obtained_hash_map[char] = char_count
        
        #print(f"expected_hash_map: {expected_hash_map}")
        #print(f"obtained_hash_map: {obtained_hash_map}")        
        result = []
        for kk, vv in obtained_hash_map.items():
            result.append(obtained_hash_map[kk] // expected_hash_map[kk])
        #print(f"RESULT: {result}")
        return min(result)
        """
