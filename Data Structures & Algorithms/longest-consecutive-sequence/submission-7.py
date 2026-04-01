class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        num_set = set(nums)
        for i in range(len(nums)):
            curr = nums[i]  
            curr_streak = 1 
            while (curr + 1) in num_set:
                curr_streak += 1
                curr += 1
        
            res = max(res, curr_streak)

        return res 
