class Solution {
    public int concatenatedBinary(int n) {
        final int MOD = 1000000007;
        long result = 0;
        int length = 0;
        
        for (int i = 1; i <= n; i++) {
            
            // If i is power of 2, increase bit length
            if ((i & (i - 1)) == 0) {
                length++;
            }
            
            // Shift left and add i
            result = ((result << length) % MOD + i) % MOD;
        }
        
        return (int) result;
    }
}