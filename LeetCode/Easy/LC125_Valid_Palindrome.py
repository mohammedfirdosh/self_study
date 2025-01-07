class Solution:
    def isPalindrome(self, s: str) -> bool:
        # https://leetcode.com/problems/valid-palindrome/
        # 2ms 99%
        if len(s) == 1: return True

        l_ptr, r_ptr = 0, len(s)-1
        s = s.lower()
        while l_ptr < r_ptr:
            #print(f"Starting with  |{s[l_ptr].lower()}| and |{s[r_ptr].lower()}| {s[l_ptr].isalnum()}| {s[r_ptr].isalnum()}")
            if not s[l_ptr].isalnum():
                #print("In first condition")
                l_ptr += 1
                continue
            if not s[r_ptr].isalnum():
                #print("In second condition")
                r_ptr -= 1
                continue
            #print(f"Comparing |{s[l_ptr].lower()}| and |{s[r_ptr].lower()}| at pointers: {l_ptr} and {r_ptr}")
            if s[l_ptr] != s[r_ptr]:
                return False
            l_ptr += 1
            r_ptr -= 1
        return True
        
