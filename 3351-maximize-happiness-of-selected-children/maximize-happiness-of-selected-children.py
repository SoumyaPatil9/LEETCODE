class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        
        total = 0
        
        for i in range(k):
            value = happiness[i] - i
            if value <= 0:
                break
            total += value
        
        return total