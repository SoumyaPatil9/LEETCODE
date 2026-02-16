class Solution {
    public int minCut(String s) {
        int n = s.length();
        
        int[] dp = new int[n];
        boolean[][] isPal = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            dp[i] = i;  // worst case: cut each character
            
            for (int j = 0; j <= i; j++) {
                if (s.charAt(j) == s.charAt(i) &&
                   (i - j <= 2 || isPal[j + 1][i - 1])) {
                    
                    isPal[j][i] = true;
                    
                    if (j == 0)
                        dp[i] = 0;
                    else
                        dp[i] = Math.min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        
        return dp[n - 1];
    }
}
