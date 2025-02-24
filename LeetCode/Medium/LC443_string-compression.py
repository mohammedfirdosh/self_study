# 443 https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write

        """
        n = len(chars)
        p1, p2 = 0, 1
        char_count = 1
        while p2 < n:
            if chars[p1] != chars[p2]:
                chars.append(chars[p1])
                if char_count > 1:
                    chars.extend(list(str(char_count)))
                char_count = 1
                p1 = p2
            else:
                char_count += 1
            p2 += 1
        else:
            chars.append(chars[p1])
            if char_count > 1:
                chars.extend(list(str(char_count)))
        del chars[:n]
        # print(f"RESULT: {chars}")
        """
