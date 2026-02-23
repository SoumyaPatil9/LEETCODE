class Solution:
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        
        total = 0
        
        # Add full weeks
        for w in range(weeks):
            total += 7 * (1 + w) + 21
        
        # Add remaining days
        start = 1 + weeks
        for d in range(days):
            total += start + d
        
        return total