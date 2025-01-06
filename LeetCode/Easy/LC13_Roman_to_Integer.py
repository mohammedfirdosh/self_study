class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = conversion_map[s[0]]
        num_len = len(s)
        if num_len < 2:
            return conversion_map.get(s[0], 0)
        ptr1, ptr2 = 0, 1
        integer_equivalent = 0
        while ptr2 < num_len:
            val1 = conversion_map[s[ptr1]]
            val2 = conversion_map[s[ptr2]]
            if  val1 >= val2:
                integer_equivalent += val1
                ptr1 += 1
                ptr2 += 1
            elif val1 < val2: 
                integer_equivalent += val2 - val1
                ptr1 += 2
                ptr2 += 2        
        else:
            if ptr1 == num_len -1:
                integer_equivalent += conversion_map[s[ptr1]]

        return integer_equivalent
        
