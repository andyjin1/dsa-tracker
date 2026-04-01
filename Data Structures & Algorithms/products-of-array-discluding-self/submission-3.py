class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = [1] * len(nums)
        postfix = 1
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        for j in range(len(nums) - 1, -1, -1):
            prefix_product[j] = prefix_product[j] * postfix
            postfix *= nums[j]
        
        return prefix_product
        # [1, 1, 2, 8]
        # [48, 24, 6,1]
        # 1 * 48, 1 * 24, 2 * 6, 8 * 1
        