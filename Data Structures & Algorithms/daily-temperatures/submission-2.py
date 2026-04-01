class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        # we can push the current temperature onto the stack
        # we only keep smaller elements on the stack, when we see a warmer temperature we can pop from the stack
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res