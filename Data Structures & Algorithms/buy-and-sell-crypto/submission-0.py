class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cost_price = math.inf
        for i in range(len(prices)):
            if prices[i] < cost_price:
                cost_price = prices[i]
            else :
                max_profit = max(max_profit, prices[i] - cost_price)
        return max_profit
            
 

        