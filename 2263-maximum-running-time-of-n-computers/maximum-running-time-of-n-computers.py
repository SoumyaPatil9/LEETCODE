class Solution:
    def maxRunTime(self, n, batteries):
        
        left = 0
        right = sum(batteries) // n   # upper bound
        
        while left <= right:
            mid = (left + right) // 2
            
            total = 0
            for b in batteries:
                total += min(b, mid)
            
            if total >= n * mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return right