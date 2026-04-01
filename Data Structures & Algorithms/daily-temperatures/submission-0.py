class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            j = i + 1 
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                    
                j += 1
        return res
