class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        res = float('-inf')
        for p in prices:
            res = max(p - min_price, res)
            min_price = min(p, min_price)
        
        return res

                   