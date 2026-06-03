class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        for l in range(n):
            for r in range(l+1, n):
                if prices[l] < prices[r]:
                    profit = prices[r] - prices[l]
                    maxprofit = max(maxprofit, profit)
                

        return maxprofit