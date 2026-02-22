class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = 0
        empty = 0
        full = numBottles
        
        while full > 0:
            # Drink all full bottles
            total_drunk += full
            empty += full
            
            # Exchange empty bottles for new full ones
            full = empty // numExchange
            empty = empty % numExchange
        
        return total_drunk