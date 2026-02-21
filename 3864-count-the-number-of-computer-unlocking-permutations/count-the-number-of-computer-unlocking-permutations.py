class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)
        
        min_so_far = complexity[0]
        
        # Check feasibility
        for i in range(1, n):
            if complexity[i] <= min_so_far:
                return 0
            min_so_far = min(min_so_far, complexity[i])
        
        # Compute (n-1)!
        result = 1
        for i in range(1, n):
            result = (result * i) % MOD
        
        return result