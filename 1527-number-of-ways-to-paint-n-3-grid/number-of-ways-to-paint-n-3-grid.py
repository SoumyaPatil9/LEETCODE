class Solution:
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        # Base case for first row
        same = 6   # ABA patterns
        diff = 6   # ABC patterns
        
        for _ in range(2, n + 1):
            new_same = (3 * same + 2 * diff) % MOD
            new_diff = (2 * same + 2 * diff) % MOD
            
            same, diff = new_same, new_diff
        
        return (same + diff) % MOD