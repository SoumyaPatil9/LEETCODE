class Solution:
    def findSmallestInteger(self, nums, value):
        from collections import Counter
        
        count = Counter()
        
        # Normalize modulo to always positive
        for num in nums:
            remainder = num % value
            count[remainder] += 1
        
        mex = 0
        
        while True:
            remainder = mex % value
            
            if count[remainder] > 0:
                count[remainder] -= 1
                mex += 1
            else:
                return mex