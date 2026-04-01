class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # add to window when the element is greater than the left most element 
        # calculate the max profit
        # remove from the window when the next element is smaller than the left most element 

        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            to_add = prices[r]
            max_profit = max(max_profit, prices[r] - prices[l])
            
            while l <= r and prices[l] > prices[r]:
                l += 1 
            r += 1
        return max_profit
    
    # prices = [7,1,5,3,6,4]

    # l = 0, r = 1 
    # max_profit = 0 
    # 
