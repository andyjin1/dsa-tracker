class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        visit = set()
        candidates.sort()
        def dfs(i, path_sum):
            
            if path_sum == target:
                res.append(path.copy())
                return 

            if i >= len(candidates) or path_sum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                path.append(candidates[j])
                dfs(j + 1, candidates[j] + path_sum)
                path.pop()
            
        dfs(0, 0)
        return res