class Solution {
    
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        
        if (n < 4) return false; // need at least 4 elements
        
        // Try all possible p and q
        for (int p = 1; p <= n - 3; p++) {
            for (int q = p + 1; q <= n - 2; q++) {
                
                if (isIncreasing(nums, 0, p) &&
                    isDecreasing(nums, p, q) &&
                    isIncreasing(nums, q, n - 1)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // Check strictly increasing from start to end
    private boolean isIncreasing(int[] nums, int start, int end) {
        for (int i = start; i < end; i++) {
            if (nums[i] >= nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
    
    // Check strictly decreasing from start to end
    private boolean isDecreasing(int[] nums, int start, int end) {
        for (int i = start; i < end; i++) {
            if (nums[i] <= nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
}