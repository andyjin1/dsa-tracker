class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visit = set()
        path = []
        n = len(nums)
        def dfs(i):
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if i not in visit:
                    path.append(nums[i])
                    visit.add(i)
                    dfs(i + 1)
                    path.pop()
                    visit.remove(i)
        dfs(0)
        
        return res