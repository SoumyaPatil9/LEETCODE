class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        
        prev = -10**18
        count = 0
        
        for num in nums:
            low = num - k
            high = num + k
            
            assign = max(low, prev + 1)
            
            if assign <= high:
                count += 1
                prev = assign
        
        return count