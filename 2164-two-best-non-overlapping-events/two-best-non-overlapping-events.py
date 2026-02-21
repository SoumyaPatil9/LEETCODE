import bisect

class Solution:
    def maxTwoEvents(self, events):
        # Sort by start time
        events.sort()
        
        n = len(events)
        
        # Store start times separately for binary search
        starts = [event[0] for event in events]
        
        # Build max_from_right array
        max_from_right = [0] * n
        max_from_right[-1] = events[-1][2]
        
        for i in range(n - 2, -1, -1):
            max_from_right[i] = max(max_from_right[i + 1], events[i][2])
        
        max_sum = 0
        
        for i in range(n):
            start, end, value = events[i]
            
            # Option 1: take only this event
            max_sum = max(max_sum, value)
            
            # Option 2: take this + next non-overlapping
            next_index = bisect.bisect_right(starts, end)
            
            if next_index < n:
                max_sum = max(max_sum, value + max_from_right[next_index])
        
        return max_sum