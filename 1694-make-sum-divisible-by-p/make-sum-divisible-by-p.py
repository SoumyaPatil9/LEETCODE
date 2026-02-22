class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        target = total_sum % p
        
        # If already divisible
        if target == 0:
            return 0
        
        prefix_mod = 0
        min_len = len(nums)
        
        # Map remainder → latest index
        remainder_index = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % p
            
            # We want:
            # (prefix_mod - target) % p
            needed = (prefix_mod - target) % p
            
            if needed in remainder_index:
                min_len = min(min_len, i - remainder_index[needed])
            
            # Store latest index
            remainder_index[prefix_mod] = i
        
        # Cannot remove whole array
        if min_len == len(nums):
            return -1
        
        return min_len