class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = 0
        max_right[-1] = 0
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for j in range(len(height) - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], height[j + 1 ])        
        
        res = 0
        
        for i in range(len(height)):
            res += max(0, min(max_left[i], max_right[i]) - height[i]) 
        
        return res



# max_left = [4,4,4,4,4,5]