class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        drunk = 0
        empty = 0
        full = numBottles
        
        while full > 0:
            # Drink all full bottles
            drunk += full
            empty += full
            full = 0
            
            # Exchange once per current numExchange value
            if empty >= numExchange:
                empty -= numExchange
                full = 1
                numExchange += 1
            else:
                break
        
        return drunk