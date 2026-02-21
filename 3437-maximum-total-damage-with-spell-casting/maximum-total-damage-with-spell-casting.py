class Solution:
    def maximumTotalDamage(self, power):
        from collections import Counter
        import bisect
        
        freq = Counter(power)
        vals = sorted(freq.keys())
        n = len(vals)
        
        # Precompute total damage for each unique value
        weight = [vals[i] * freq[vals[i]] for i in range(n)]
        
        dp = [0] * n
        
        for i in range(n):
            # Option 1: take current
            take = weight[i]
            
            # Find last index j where vals[j] <= vals[i] - 3
            target = vals[i] - 3
            j = bisect.bisect_right(vals, target) - 1
            
            if j >= 0:
                take += dp[j]
            
            # Option 2: skip
            skip = dp[i - 1] if i > 0 else 0
            
            dp[i] = max(skip, take)
        
        return dp[-1]