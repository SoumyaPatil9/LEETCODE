class Solution:
    def countPartitions(self, nums):
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return 0
        
        return len(nums) - 1