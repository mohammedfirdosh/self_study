# 135: https://leetcode.com/problems/candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        #print(f"Initial candies: {candies}")
        
        # Left-to-Right Pass
        for i in range(1, n):
            print(f"L-R: Comparing ratings[{i}]: {ratings[i]}  ratings[{i - 1}]: {ratings[i-1]}")
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        print(f"Left-Right pass: {candies}")
        
        # Right-to-Left Pass
        for i in range(n - 2, -1, -1):
            print(f"R-L: Comparing ratings[{i}]: {ratings[i]}  ratings[{i + 1}]: {ratings[i+1]}")            
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        print(f"Right-Left pass: {candies}")
        
        return sum(candies)        
