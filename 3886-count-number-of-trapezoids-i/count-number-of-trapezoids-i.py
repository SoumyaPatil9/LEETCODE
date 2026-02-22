class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        from collections import defaultdict
        
        y_count = defaultdict(int)
        
        # Count points per y-coordinate
        for x, y in points:
            y_count[y] += 1
        
        pair_counts = []
        
        # Calculate C(n,2) for each y having at least 2 points
        for count in y_count.values():
            if count >= 2:
                pair_counts.append(count * (count - 1) // 2)
        
        if len(pair_counts) < 2:
            return 0
        
        total_sum = sum(pair_counts) % MOD
        square_sum = sum((p * p) % MOD for p in pair_counts) % MOD
        
        result = (total_sum * total_sum - square_sum) % MOD
        
        # Divide by 2 using modular inverse
        result = result * pow(2, MOD - 2, MOD) % MOD
        
        return result