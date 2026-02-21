class Solution:
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict
        
        # Build mapping: (left, right) -> possible tops
        allowed_map = defaultdict(list)
        for pattern in allowed:
            allowed_map[pattern[:2]].append(pattern[2])
        
        memo = {}
        
        def can_build(curr):
            if len(curr) == 1:
                return True
            
            if curr in memo:
                return memo[curr]
            
            # Generate all possible next rows
            possible_rows = []
            
            def backtrack(index, path):
                if index == len(curr) - 1:
                    possible_rows.append(path)
                    return
                
                pair = curr[index:index+2]
                if pair not in allowed_map:
                    return
                
                for ch in allowed_map[pair]:
                    backtrack(index + 1, path + ch)
            
            backtrack(0, "")
            
            # Try each possible next row
            for row in possible_rows:
                if can_build(row):
                    memo[curr] = True
                    return True
            
            memo[curr] = False
            return False
        
        return can_build(bottom)