class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        prefix_product = [1] * len(nums)
        postfix_product = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            postfix_product[j] = postfix_product[j + 1] * nums[j + 1]
            
        for i in range(len(nums)):
            res[i] = prefix_product[i] * postfix_product[i]
        
        return res
        # [1, 1, 2, 8]
        