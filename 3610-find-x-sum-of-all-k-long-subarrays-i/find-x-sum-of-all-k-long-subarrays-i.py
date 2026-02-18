class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            
            # Count frequency
            freq = {}
            for num in window:
                freq[num] = freq.get(num, 0) + 1
            
            # Sort by frequency desc, value desc
            sorted_elements = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            # If distinct elements less than x
            if len(sorted_elements) <= x:
                result.append(sum(window))
            else:
                total = 0
                # Take top x elements
                for j in range(x):
                    value, count = sorted_elements[j]
                    total += value * count
                result.append(total)
        
        return result
