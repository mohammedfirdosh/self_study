class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 25ms Beats 91.50%

        max_profit = 0
        min_price = float("inf")

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if  profit > max_profit:
                max_profit = profit
        return max_profit


        """
        # 139ms Beats 16.42%
        max_profit = 0
        min_price = float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max (price - min_price, max_profit)
            #print(f"price: {price} | min_price: {min_price} | max_profit: {max_profit}")
        return max_profit
        """
        """
        current_profit = final_profit = 0
        for buy_day in range(len(prices) -1):
            for sell_day in range(buy_day + 1, len(prices)):
                #print(f"Comapring days--> buy_day: {buy_day} | sell_day: {sell_day} | corresponding prices: {prices[sell_day]} and {prices[buy_day]}")
                current_profit = max(current_profit, prices[sell_day] - prices[buy_day])
            final_profit = max(final_profit, current_profit)
        
        return final_profit
        """
