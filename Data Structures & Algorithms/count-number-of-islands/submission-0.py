class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of runs in dfs is the number of islands
        m, n = len(grid), len(grid[0])
        island_count = 0    
        dirs = (0,1),(1,0),(0,-1),(-1,0)

        def dfs(i, j):
            if grid[i][j] == "0":
                return 
            
            grid[i][j] = "0"

            for dx, dy in dirs:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    dfs(new_x, new_y)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        
        return island_count