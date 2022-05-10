class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n), O(1)
        
        res = 0
        l, r = 0,1
        
        while r < len(prices):
            p = prices[r] - prices[l]
            res = max(res, p)
            
            # when current price is less than the previous buying price, update the buying price 
            if prices[r] < prices[l]:
                l = r
            r +=1
            
        return res 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not prices or len(prices) == 1: return 0
        # max_profit, min_price = 0, float("inf")
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        # return max_profit
        