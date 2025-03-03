# 679: https://leetcode.com/problems/24-game
# https://www.youtube.com/watch?v=I_Ikfbeop8I
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)

        if n == 1:
            if abs(cards[0] - 24) < 1e-6:
                return True
            return False

        for ii in range(n):
            for jj in range(ii + 1, n):
                c1 = cards[ii]
                c2 = cards[jj]

                possible_results = [c1 + c2, c1 - c2, c2 - c1, c1 * c2]
                if c1:
                    possible_results.append(c2 / c1)
                if c2:
                    possible_results.append(c1 / c2)

                for vv in possible_results:
                    next_cards = [vv]

                    for kk in range(n):
                        if kk not in [ii, jj]:
                            next_cards.append(cards[kk])

                    if self.judgePoint24(next_cards):
                        return True
        return False
