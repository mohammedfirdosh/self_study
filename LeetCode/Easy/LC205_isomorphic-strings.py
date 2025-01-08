class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # https://leetcode.com/problems/isomorphic-strings
        
        if len(s) != len(t):
            return False
        
        char_s_idx = dict()
        char_t_idx = dict()

        for idx in range(len(s)):
            if s[idx] not in char_s_idx:
                char_s_idx[s[idx]] = idx
            
            if t[idx] not in char_t_idx:
                char_t_idx[t[idx]] = idx

            if char_s_idx[s[idx]] != char_t_idx[t[idx]]:

                return False
        return True

        """
        # 7ms 58%
        if len(s) != len(t):
            return False
        
        mapST = [-1] * 256
        mapTS = [-1] * 256
        
        for chS, chT in zip(s, t):
            if mapST[ord(chS)] == -1 and mapTS[ord(chT)] == -1:
                mapST[ord(chS)] = ord(chT)
                mapTS[ord(chT)] = ord(chS)
            elif mapST[ord(chS)] != ord(chT) or mapTS[ord(chT)] != ord(chS):
                return False
        
        return True        
        """
