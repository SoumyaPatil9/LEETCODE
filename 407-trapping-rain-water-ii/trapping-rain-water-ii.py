import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        if m < 3 or n < 3:
            return 0  # Cannot trap water
        
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Step 1: Add all boundary cells to heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        total_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: Process cells
        while heap:
            height, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    # Water trapped
                    if heightMap[nx][ny] < height:
                        total_water += height - heightMap[nx][ny]
                    
                    # Push with updated height
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return total_water