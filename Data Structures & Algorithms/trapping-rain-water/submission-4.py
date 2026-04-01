class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = height[0], height[-1]
        left, right = 0, len(height) - 1
        res = 0 

        while left < right:
            if max_left <= max_right:
                left += 1 
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            
            else:
                right -= 1 
                max_right = max(max_right, height[right])
                res += max_right - height[right]
        
        return res