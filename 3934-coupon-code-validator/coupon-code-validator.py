class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        n = len(code)
        
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid = []
        
        for i in range(n):
            # Must be active
            if not isActive[i]:
                continue
            
            # Valid business line
            if businessLine[i] not in order:
                continue
            
            # Code must be non-empty
            if not code[i]:
                continue
            
            # Code must contain only alphanumeric or underscore
            ok = True
            for ch in code[i]:
                if not (ch.isalnum() or ch == "_"):
                    ok = False
                    break
            
            if not ok:
                continue
            
            valid.append((order[businessLine[i]], code[i]))
        
        # Sort by business order then lexicographically
        valid.sort(key=lambda x: (x[0], x[1]))
        
        return [x[1] for x in valid]