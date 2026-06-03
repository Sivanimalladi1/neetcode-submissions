class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        l =0 
        r = 1
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
            else:
                l = r 
            r = r + 1
                

        return maxprofit