class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       # 0ms Beats 100.00%
        
        result = ""
        min_length = min(len(s) for s in strs)
        for idx in range(min_length):
            if len(set(element[idx] for element in strs)) == 1:
                result += strs[0][idx]
            else:
                break
        return result
