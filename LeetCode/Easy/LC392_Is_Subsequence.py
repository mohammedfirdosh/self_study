class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        if s == '': return True
        if S > T: return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        
        return False

        """
        ptr_s = ptr_t = 0
        len_t = len(t)
        len_s = len(s)

        while ptr_t < len_t and ptr_s < len_s:
            #print(f"Comparing s: {s[ptr_s]} and t: {t[ptr_t]}")
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
            #print(f"AFTER: Value of pointers ptr_s: {ptr_s} and ptr_t: {ptr_t}")
        else:
            if ptr_t == len_t and ptr_s < len_s:
                return False
            return True    
        
        return False
        """
