class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        maxProfit = 0
        curr = 0 
        
        for right in range(1,len(prices)):

            if prices[left] >= prices[right]:
                left = right
            
            curr = prices[right] - prices[left]
            maxProfit = max(curr,maxProfit)
        
        return maxProfit

            


        