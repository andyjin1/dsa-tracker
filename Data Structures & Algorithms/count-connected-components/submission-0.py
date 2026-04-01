class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc_count = 0 
        adj = [[] for _ in range(n)]
        visit = [False] * n
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(x):
            if visit[x]:
                return 
            
            visit[x] = True 

            for nei in adj[x]:
                dfs(nei)
        
        for i in range(n):
            if not visit[i]:
                dfs(i)  
                cc_count += 1
        
        return cc_count