class Solution:
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        
        prefix = 0
        ans = float('-inf')
        
        # For each remainder, store minimum prefix sum
        min_prefix = {}
        min_prefix[0] = 0  # prefix before starting
        
        for i in range(1, n + 1):
            prefix += nums[i - 1]
            
            remainder = i % k
            
            if remainder in min_prefix:
                ans = max(ans, prefix - min_prefix[remainder])
                min_prefix[remainder] = min(min_prefix[remainder], prefix)
            else:
                min_prefix[remainder] = prefix
        
        return ans
