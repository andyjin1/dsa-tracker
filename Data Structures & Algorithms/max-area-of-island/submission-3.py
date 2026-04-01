class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        dirs = (0,1), (1,0),(0,-1),(-1,0)
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal curr_area
            
            grid[i][j] = 0
            curr_area += 1
            
            for dx, dy in dirs:
                new_x, new_y = i + dx, j + dy 

                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_area = 0
                    dfs(i, j)
                    max_area = max(max_area, curr_area)
        
        return max_area
            