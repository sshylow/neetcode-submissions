class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        max_profit = 0

        for price in prices:
            profit_if_sold_today = price - lowest_price
            max_profit = max(max_profit, profit_if_sold_today)
            lowest_price = min(lowest_price, price)

        return max_profit