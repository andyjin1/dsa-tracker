class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack that stores (temperatures, index)
        
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                val, idx = stack.pop()  
                res[idx] = i - idx 
            stack.append((t,i))
        
        return res
                