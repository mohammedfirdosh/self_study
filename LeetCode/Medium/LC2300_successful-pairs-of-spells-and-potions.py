# 2300: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/submissions/1554067750/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []
        
        for spell in spells:
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if spell * potions[mid] >= success:
                    right = mid -1
                else:
                    left = mid + 1
            result.append(n - left)
        
        return result

        """
        result = list()
        n = len(potions)
        potions.sort()
        for spell in spells:
            if spell * potions[0] >= success:
                result.append(n)
                continue
            elif spell * potions[n - 1] < success:
                result.append(0)
                continue
            else:
                l, r = 0, n - 1
                while l <= r:
                    m = l + (r - l) // 2
                    #print(
                    #    f"Working with spell: {spell} and potion: {potions[m]} | prod: {spell * potions[m]} and success: {success}| l:{l}, r:{r} & m:{m}"
                    #)
                    if spell * potions[m] >= success:
                        r = m - 1
                    else:
                        l = m + 1
                #print(f"Found boundary with l:{l}. Saving: {n-l+1}")
                result.append(n - l)
        return result
        """
