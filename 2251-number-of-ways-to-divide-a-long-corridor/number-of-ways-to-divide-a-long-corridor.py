class Solution:
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        
        seat_positions = []
        
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seat_positions.append(i)
        
        total_seats = len(seat_positions)
        
        # If no seats or odd seats → impossible
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        
        ways = 1
        
        # For every boundary between seat pairs
        for i in range(2, total_seats, 2):
            plants_between = seat_positions[i] - seat_positions[i-1] - 1
            ways = (ways * (plants_between + 1)) % MOD
        
        return ways