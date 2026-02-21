class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        half = k // 2
        
        # Original profit
        original = 0
        for i in range(n):
            original += strategy[i] * prices[i]
        
        # Precompute gain arrays
        left_gain = [0] * n
        right_gain = [0] * n
        
        for i in range(n):
            left_gain[i] = -strategy[i] * prices[i]
            right_gain[i] = (1 - strategy[i]) * prices[i]
        
        # Prefix sums
        prefix_left = [0] * (n + 1)
        prefix_right = [0] * (n + 1)
        
        for i in range(n):
            prefix_left[i+1] = prefix_left[i] + left_gain[i]
            prefix_right[i+1] = prefix_right[i] + right_gain[i]
        
        max_gain = 0
        
        # Slide window
        for l in range(n - k + 1):
            mid = l + half
            r = l + k
            
            gain = (
                prefix_left[mid] - prefix_left[l]
                + prefix_right[r] - prefix_right[mid]
            )
            
            if gain > max_gain:
                max_gain = gain
        
        return max(original, original + max_gain)