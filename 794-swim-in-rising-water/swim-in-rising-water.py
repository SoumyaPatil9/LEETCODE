import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time, x, y)
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            time, x, y = heapq.heappop(heap)
            
            if x == n-1 and y == n-1:
                return time
            
            if visited[x][y]:
                continue
            
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    new_time = max(time, grid[nx][ny])
                    heapq.heappush(heap, (new_time, nx, ny))