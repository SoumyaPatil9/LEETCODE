class Solution:
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        
        # dp[j] represents current row
        dp = [0] * (n + 1)
        
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    new_dp[j] = ord(s1[i]) + dp[j + 1]
                else:
                    new_dp[j] = max(dp[j], new_dp[j + 1])
            dp = new_dp
        
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        return total - 2 * dp[0]