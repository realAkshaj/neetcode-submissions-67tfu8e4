class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currWindow, maxProfit, l,r = 0,0,0,1

        while r < len(prices):

            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                maxProfit = max(profit,maxProfit)
            else:
                l = r            
            r += 1
        
        return maxProfit






            

        