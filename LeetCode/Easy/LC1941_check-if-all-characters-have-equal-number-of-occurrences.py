# LC 1941 : https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/?envType=problem-list-v2&envId=hash-table
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        m=s.count(s[0])
        for i in set(s):
            if s.count(i)!=m: return False
        return True

        """
        my_dict = {}
        for c in s:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        if len(my_dict) ==1:
            return True
        first_value = next(iter(my_dict.values()))
        return all(value == first_value for value in my_dict.values())
        """
