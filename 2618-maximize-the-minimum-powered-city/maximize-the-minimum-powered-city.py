class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        
        # Step 1: Compute initial power
        power = [0] * n
        diff = [0] * (n + 1)
        
        for i, val in enumerate(stations):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            diff[left] += val
            diff[right + 1] -= val
        
        curr = 0
        for i in range(n):
            curr += diff[i]
            power[i] = curr
        
        # Step 2: Binary search
        left, right = 0, sum(stations) + k
        answer = 0
        
        def canAchieve(target):
            used = 0
            added = [0] * (n + 1)
            curr_add = 0
            
            temp_power = power[:]  # copy
            
            for i in range(n):
                curr_add += added[i]
                total = temp_power[i] + curr_add
                
                if total < target:
                    need = target - total
                    used += need
                    if used > k:
                        return False
                    
                    curr_add += need
                    end = min(n, i + 2*r + 1)
                    added[end] -= need
            
            return True
        
        while left <= right:
            mid = (left + right) // 2
            
            if canAchieve(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer