class Solution:
    def getDescentPeriods(self, prices):
        n = len(prices)
        count = 0
        streak = 1  # single element is always valid
        
        for i in range(n):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                streak = 1
            
            count += streak
        
        return count
