class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        transaction_price = 0
    
        for i in range(len(prices)): #buy date
            for j in range(i+1, len(prices)): #sell date
                transaction_price = max(transaction_price, prices[j]-prices[i])

        return transaction_price