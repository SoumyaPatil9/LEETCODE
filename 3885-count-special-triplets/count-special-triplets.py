class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        from collections import defaultdict
        
        left = defaultdict(int)
        right = defaultdict(int)
        
        # Count frequency of all elements (initially all are on right)
        for num in nums:
            right[num] += 1
        
        ans = 0
        
        for num in nums:
            # Current element becomes middle, remove from right
            right[num] -= 1
            
            target = 2 * num
            
            # Count valid triplets
            ans = (ans + left[target] * right[target]) % MOD
            
            # Add current to left side
            left[num] += 1
        
        return ans