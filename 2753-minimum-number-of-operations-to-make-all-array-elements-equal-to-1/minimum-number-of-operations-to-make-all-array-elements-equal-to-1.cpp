class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        
        // Count existing 1s
        int count1 = 0;
        for (int x : nums) {
            if (x == 1) count1++;
        }
        
        // Case 1: Already have 1
        if (count1 > 0) {
            return n - count1;
        }
        
        // Case 2: No 1, find shortest subarray with gcd = 1
        int minLen = INT_MAX;
        
        for (int i = 0; i < n; i++) {
            int g = nums[i];
            for (int j = i; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    minLen = min(minLen, j - i + 1);
                    break;
                }
            }
        }
        
        if (minLen == INT_MAX) return -1;
        
        return (minLen - 1) + (n - 1);
    }
};
