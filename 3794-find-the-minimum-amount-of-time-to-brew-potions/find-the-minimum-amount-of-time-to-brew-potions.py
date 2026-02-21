class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)
        
        # Prefix sums of skill
        prefix = [0] * n
        prefix[0] = skill[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + skill[i]
        
        start_prev = 0  # start time of previous potion
        
        for j in range(1, m):
            best = 0
            for i in range(n):
                left = prefix[i] * mana[j - 1]
                right = (prefix[i - 1] if i > 0 else 0) * mana[j]
                best = max(best, left - right)
            
            start_prev += best
        
        # Finish time of last potion
        return start_prev + prefix[n - 1] * mana[m - 1]