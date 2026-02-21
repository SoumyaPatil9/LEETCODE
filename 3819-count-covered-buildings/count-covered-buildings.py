import bisect
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n, buildings):
        # Group buildings by row and column
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # Sort each row and column group
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()
        
        covered = 0
        
        for x, y in buildings:
            row_list = rows[x]
            col_list = cols[y]
            
            # Find position using binary search
            col_index = bisect.bisect_left(row_list, y)
            row_index = bisect.bisect_left(col_list, x)
            
            # Check left and right
            has_left = col_index > 0
            has_right = col_index < len(row_list) - 1
            
            # Check above and below
            has_up = row_index > 0
            has_down = row_index < len(col_list) - 1
            
            if has_left and has_right and has_up and has_down:
                covered += 1
        
        return covered