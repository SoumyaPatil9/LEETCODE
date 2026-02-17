class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        
        for i in range(n - 2 * k + 1):
            first = all(nums[j] < nums[j+1] for j in range(i, i+k-1))
            second = all(nums[j] < nums[j+1] for j in range(i+k, i+2*k-1))
            
            if first and second:
                return True
        
        return False
