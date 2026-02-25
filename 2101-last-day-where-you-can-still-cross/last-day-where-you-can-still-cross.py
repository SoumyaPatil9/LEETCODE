from collections import deque

class Solution:
    def latestDayToCross(self, row, col, cells):
        
        def can_cross(day):
            # Create grid
            grid = [[0] * col for _ in range(row)]
            
            # Flood first 'day' cells
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1  # water
            
            # BFS from top row
            q = deque()
            visited = set()
            
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    visited.add((0, c))
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                r, c = q.popleft()
                
                if r == row - 1:  # reached bottom
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 0 <= nc < col and
                        grid[nr][nc] == 0 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            return False
        
        # Binary search
        left, right = 1, row * col
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans