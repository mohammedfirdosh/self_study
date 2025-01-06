class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 17.61MB | Beats 25.38%
        return sum(1 for stone in stones if stone in jewels)
        """
        # 17.74MB | Beats 16.3%
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
        """
        """
        # 0ms Beats 100% | 17.96 MB Beats 9.99%
        jewel_map =  {char: 0 for char in set(jewels)}
        for stone in stones:
            if stone in jewel_map:
                jewel_map[stone] += 1
        return sum(jewel_map.values())
        """

        
