class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(i, path_sum):
            if path_sum == target:
                res.append(path[:])
            if path_sum > target or i >= len(nums): 
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, path_sum + nums[j])
                path.pop()

        dfs(0,0)
        return res