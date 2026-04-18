class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,n = 0,1,len(prices)
        maxprofit = 0
        while r<n:
            if prices[r]>prices[l]:
                maxprofit = max(maxprofit, prices[r]-prices[l])
            else:
                l = r
            r+=1
            
        return maxprofit