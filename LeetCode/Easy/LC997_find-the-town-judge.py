# LC 997: https://leetcode.com/problems/find-the-town-judge/?envType=problem-list-v2&envId=graph
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_scores = [0] * (n + 1)
        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1
        # print(f"trust_scorees: {trust_scores}")
        for ii in range(1, n + 1):
            if trust_scores[ii] == n - 1:
                return ii
        return -1
