class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        postfix = [1] * len(nums)
        prefix = 1 

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            postfix[i] = postfix[i] * prefix 
            prefix *= nums[i]
        
        return postfix