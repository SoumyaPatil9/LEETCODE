class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m = len(heights)
        n = len(heights[0])
        
        from collections import deque
        
        def bfs(starts):
            visited = [[False] * n for _ in range(m)]
            queue = deque(starts)
            
            for r, c in starts:
                visited[r][c] = True
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < m and 0 <= nc < n and
                        not visited[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            
            return visited
        
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]
        
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        
        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result