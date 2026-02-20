class Solution:
    def minOperations(self, nums, k):
        # Calculate total sum
        total_sum = sum(nums)
        
        # Minimum operations needed
        return total_sum % k
