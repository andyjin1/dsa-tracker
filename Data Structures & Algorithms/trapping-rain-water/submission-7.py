class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_l, max_r = 0, 0

        l, r = 0, len(height) - 1
        res = 0 
        while l < r: 
            if height[l] <= height[r]:
                max_l = max(height[l], max_l)
                res += max_l - height[l]
                l += 1

            else:
                max_r = max(height[r], max_r)
                res += max_r - height[r]
                r -= 1
        
        return res