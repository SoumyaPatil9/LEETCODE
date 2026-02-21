class Solution:
    def bestClosingTime(self, customers):
        penalty = customers.count('Y')  # close at hour 0
        min_penalty = penalty
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:  # 'N'
                penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
        
        return best_hour