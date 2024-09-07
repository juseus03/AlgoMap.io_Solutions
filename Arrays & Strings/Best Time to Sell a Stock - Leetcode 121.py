from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

# Test cases
sol = Solution()

prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

prices = [7,6,4,3,1]
print(sol.maxProfit(prices))