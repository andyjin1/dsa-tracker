class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        
        state = [False] * numCourses
        def dfs(x: int) -> bool:
            if state[x] == 2:
                return False 
            state[x] = 1 
            for nei in g[x]:
                if state[nei] == 1 or dfs(nei):
                    return True
            state[x] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False 
        
        return True
        
            
        