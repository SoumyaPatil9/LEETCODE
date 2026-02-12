class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        int i = 1;

        // Phase 1: strictly increasing
        while (i < n && nums[i] > nums[i - 1]) {
            i++;
        }

        // must have at least one increasing step
        if (i == 1 || i == n) return false;

        // Phase 2: strictly decreasing
        int decStart = i;
        while (i < n && nums[i] < nums[i - 1]) {
            i++;
        }

        // must have at least one decreasing step
        if (i == decStart || i == n) return false;

        // Phase 3: strictly increasing
        int inc2Start = i;
        while (i < n && nums[i] > nums[i - 1]) {
            i++;
        }

        // must reach end and have at least one step
        return (i == n && inc2Start < n);
    }
};
