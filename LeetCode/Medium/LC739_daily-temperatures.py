# LC 739: https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        st = list()
        for idx in range(n):
            while st and temperatures[idx] > temperatures[st[-1]]:
                prev_day = st.pop()
                result[prev_day] = idx - prev_day
            st.append(idx)
        return result
