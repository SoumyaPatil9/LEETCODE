class Solution:
    def intersectionSizeTwo(self, intervals):
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        chosen = []
        
        for l, r in intervals:
            # Count how many already inside
            count = 0
            for num in chosen:
                if l <= num <= r:
                    count += 1
            
            # Add missing numbers
            need = 2 - count
            
            while need > 0:
                # Add largest possible numbers
                val = r - (need - 1)
                chosen.append(val)
                need -= 1
        
        return len(chosen)