class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # https://leetcode.com/problems/reverse-string/submissions/1500259338/
        # 1ms 55%
        l_ptr, r_ptr = 0, len(s) -1

        while l_ptr < r_ptr:
            s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]
            l_ptr += 1
            r_ptr -= 1
