class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = (0,1), (1,0), (-1,0), (0, -1)

        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            
            if grid[i][j] == '1':
                grid[i][j] = '0'
        
            for dx, dy in dirs:
                new_x, new_y = i + dx, j + dy

                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)
                
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
    
        return res