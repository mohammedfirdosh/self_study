# 1011: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #print(f"Weights: {weights}")

        def load_calc(weight_per_ship):
            added_weight = 0
            day_count = 0
            for w in weights:
                added_weight += w
                #print(
                #    f"Weight per ship: {weight_per_ship} | Adding current weight: {w} | Added weight: {added_weight}"
                #)
                if added_weight > weight_per_ship:
                    day_count += 1
                    #print(f"Shipment limit reached: {added_weight} |", end="")
                    added_weight = w
                    #print(f"Unloaded {w}, Days as of now: {day_count}")
            else:
                day_count += 1
            #print(f"LOAD_CALC: day_count: {day_count}")
            return day_count <= days

        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            #print(l, r, m)
            #print(f"Trying with weight: {m} | ")
            if load_calc(m):
                #print(f"Could complete with weight {m} within {days} days")
                r = m
            else:
                #print(f"Couldn't complete with weight {m} within {days} days")
                l = m + 1
        return l
