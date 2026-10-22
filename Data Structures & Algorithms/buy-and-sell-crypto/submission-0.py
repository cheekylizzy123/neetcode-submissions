class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window approach 
        min_p = prices[0]
        profit = 0 
        for p in range(1,len(prices)):
            current_p = prices[p]
            if current_p < min_p:
                min_p = current_p
            profit = max(profit, current_p - min_p)
        
        return profit 

            