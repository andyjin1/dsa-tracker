class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we can do a mask on each recursion depth

        path = []
        mask = set()
        res = []

        def dfs():
            
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            

            for i in range(len(nums)):
                if i in mask:
                    continue 
                
                mask.add(i)
                path.append(nums[i])
                dfs()
                path.pop()
                mask.remove(i)
        dfs()
        return res