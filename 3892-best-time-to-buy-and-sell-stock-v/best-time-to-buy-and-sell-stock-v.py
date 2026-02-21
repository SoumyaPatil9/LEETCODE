class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        
        if k == 0:
            return 0
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for t in range(1, k + 1):
            best_buy = -prices[0]
            best_short = prices[0]
            
            for i in range(1, n):
                # carry forward
                dp[t][i] = dp[t][i-1]
                
                # normal transaction
                dp[t][i] = max(dp[t][i], prices[i] + best_buy)
                
                # short selling transaction
                dp[t][i] = max(dp[t][i], best_short - prices[i])
                
                # update helpers
                best_buy = max(best_buy, dp[t-1][i-1] - prices[i])
                best_short = max(best_short, dp[t-1][i-1] + prices[i])
        
        return dp[k][n-1]