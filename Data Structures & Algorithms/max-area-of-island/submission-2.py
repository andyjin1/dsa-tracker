class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = float("-inf")
        dirs = (0,1), (1,0), (0,-1), (-1,0)
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal island_size
            if grid[i][j] == 0: 
                return 
            grid[i][j] = 0
            island_size += 1    

            for dx, dy in dirs:
                new_x = i + dx
                new_y = j + dy 
            
                if 0 <= new_x < m and 0 <= new_y < n:
                    dfs(new_x, new_y)
                
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size = 0
                    dfs(i, j)
                    res = max(res, island_size)
            

        return res if res > float("-inf") else 0 