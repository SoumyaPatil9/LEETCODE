import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        
        # Min heap of available rooms
        available = list(range(n))
        heapq.heapify(available)
        
        # Min heap of busy rooms (end_time, room_number)
        busy = []
        
        # Count meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that finished before current start
            while busy and busy[0][0] <= start:
                finish_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                # Assign lowest-numbered room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting
                finish_time, room = heapq.heappop(busy)
                new_end = finish_time + duration
                heapq.heappush(busy, (new_end, room))
            
            count[room] += 1
        
        # Return room with max meetings (lowest index if tie)
        return count.index(max(count))